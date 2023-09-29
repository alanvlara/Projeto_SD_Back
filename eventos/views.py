from rest_framework import serializers
from rest_framework import viewsets
from django.utils import timezone
from pytz import timezone as pytz_timezone
from eventos.models import Evento
from utils.permissions import IsOwnerOrReadOnly
from utils.validators import valida_esporte

brasilia_timezone = pytz_timezone('America/Sao_Paulo')

class EventosReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'titulo', 'data', 'esporte', 'usuario', 'qr_code', 'link')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        user = self.context['request'].user
        usuario_associado = instance.usuario
        
        # Verifique se o usuário é o usuário associado ou é um membro da equipe.
        if user != usuario_associado and not user.is_staff:
            data.pop('qr_code')
        
        return data

class EventosWriteSerializer(serializers.ModelSerializer):
    qr_code = serializers.URLField(allow_null=True, read_only=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    link = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = Evento
        fields = ('id', 'titulo', 'link', 'data', 'esporte', 'usuario', 'qr_code')

    def create(self, validated_data):
        user = validated_data['usuario']

        if not user.criador:
            raise serializers.ValidationError("O usuário não pode criar eventos porque não é um criador.")
        
        if not valida_esporte(validated_data.get('esporte')):
            raise serializers.ValidationError("Esporte inválido.")
        
        titulo = validated_data.get('titulo')
        data = validated_data.get('data')
        validated_data['representa'] = user.representa
        qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?data={titulo}&size=200x200"
        validated_data['qr_code'] = qr_code_url

        data_atual_brasilia = timezone.now().astimezone(brasilia_timezone).date()
        # Verificar se a data é maior ou igual à data atual em Brasília
        if data < data_atual_brasilia:
            raise serializers.ValidationError("A data do evento deve ser igual ou superior à data atual.")

        evento_existente = Evento.objects.filter(titulo=titulo, data=data, representa=user.representa).exists()
        if evento_existente:
            raise serializers.ValidationError("Evento com mesmo título e data já existe.")
        
        # Crie o evento se não existir um evento com o mesmo título e data
        evento = Evento.objects.create(**validated_data)
        return evento

    def update(self, instance, validated_data):
        user = self.context['request'].user
        usuario_associado = instance.usuario
        titulo = validated_data.get('titulo', instance.titulo)
        data = validated_data.get('data')
        data_atual_brasilia = timezone.now().astimezone(brasilia_timezone).date()

        if user != usuario_associado:
            raise serializers.ValidationError("Você não tem permissão para atualizar este evento.")
        
        # Verificar se a data é maior ou igual à data atual em Brasília
        if data < data_atual_brasilia:
            raise serializers.ValidationError("A data do evento deve ser igual ou superior à data atual.")

        evento_existente = Evento.objects.filter(titulo=titulo, data=data, representa=user.representa).exists()
        if evento_existente:
            raise serializers.ValidationError("Evento com mesmo título e data já existe.")
        
        # Atualize o QR code apenas se o título for alterado
        if titulo != instance.titulo:
            qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?data={titulo}&size=200x200"
            instance.qr_code = qr_code_url
        
        instance.titulo = titulo
        instance.link = validated_data.get('link', instance.link)
        instance.data = validated_data.get('data', instance.data)
        instance.esporte = validated_data.get('esporte', instance.esporte)
        instance.save()
        
        return instance

class EventoView(viewsets.ModelViewSet):
    queryset = Evento.objects.all() 
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EventosReadSerializer
        return EventosWriteSerializer

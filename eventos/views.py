from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer, MultiPartRenderer
from django.utils import timezone
from pytz import timezone as pytz_timezone

from eventos.models import Evento
from utils.permissions import IsOwnerOrReadOnly
from utils.validators import valida_esporte

brasilia_timezone = pytz_timezone('America/Sao_Paulo')

# Create your views here.
class EventosSerializer(serializers.ModelSerializer):
    qr_code = serializers.URLField(allow_null=True, read_only=True)
    
    class Meta:
        model = Evento
        fields = ('id', 'titulo', 'link', 'data', 'esporte', 'usuario', 'qr_code')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        user = self.context['request'].user
        usuario_associado = instance.usuario
        
        if user != usuario_associado:
            data.pop('qr_code')
        
        return data

        
    def create(self, validated_data):
        
        user = self.context['request'].user

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
        # Verificar se a data é maior ou igual à data atual em brasilia
        if data < data_atual_brasilia:
            raise serializers.ValidationError("A data do evento deve ser igual ou superior à data atual.")

        evento_existente = Evento.objects.filter(titulo=titulo, data=data, representa=user.representa).exists()
        if evento_existente:
            raise serializers.ValidationError("Evento com mesmo título e data já existe.")
        
        # Crie o evento se não existir um evento com o mesmo título e data
        evento = Evento.objects.create(**validated_data)
        return evento
    
class EventoView(viewsets.ModelViewSet):
    queryset = Evento.objects.all() 
    serializer_class = EventosSerializer  
    permission_classes = [IsOwnerOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    renderer_classes = [JSONRenderer, MultiPartRenderer]
    http_method_names = ['get', 'post', 'put', 'delete']
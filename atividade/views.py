from atividade.models import Atividade
from usuario.views import UsuarioReadSerializer
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS
from utils.permissions import IsOwnerOrReadOnly
from django.utils import timezone
from pytz import timezone as pytz_timezone
from eventos.views import EventosCreateGetSerializer
from django.contrib.auth.models import AnonymousUser

brasilia_timezone = pytz_timezone('America/Sao_Paulo')

class AtividadeWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Atividade
        fields = ('id', 'data', 'evento', 'foto')  

    def create(self, validated_data):
        
        # Pega o usuário logado
        usuario = self.context['request'].user
        validated_data['usuario'] = usuario

        #Pega o Evento informado e a data dele
        evento = validated_data.get('evento')
        data_evento = evento.data if evento else None

        #Verifica se a atividade existe
        atividade_existente = Atividade.objects.filter(evento=evento, usuario=usuario).first()
        if atividade_existente:
            raise serializers.ValidationError("Já existe uma atividade para este evento e usuário.")

        # Pega a data e hora atual com o fuso horário de Brasília e verifica a data
        data_atual_brasilia = timezone.now().astimezone(brasilia_timezone).date()
        if data_evento and data_evento != data_atual_brasilia:
            raise serializers.ValidationError("A atividade só pode ser criada para um evento que ocorre na data atual (hoje) em Brasília.")

        if (evento.esporte == usuario.esportePreferido and usuario.is_active):
            usuario.totalEventos += 1
            usuario.save()

        return super().create(validated_data)



class AtividadeReadSerializer(serializers.ModelSerializer):
    usuario = UsuarioReadSerializer()
    evento = EventosCreateGetSerializer()

    class Meta:
        model = Atividade
        fields = ('id', 'usuario', 'data', 'evento', 'foto')


class AtividadeView(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeReadSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [IsOwnerOrReadOnly]  # Aplicando a permissão personalizada

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return super().get_serializer_class()
        return AtividadeWriteSerializer

    def get_queryset(self):
        # Verifica se o usuário está autenticado antes de tentar filtrar
        if not isinstance(self.request.user, AnonymousUser):
            return Atividade.objects.filter(usuario=self.request.user)
        else:
            return Atividade.objects.none()  # Retorna uma queryset vazia se o usuário não estiver autenticado
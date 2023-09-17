from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS
import base64
from usuario.models import Usuario
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer, MultiPartRenderer
from atividade.models import Atividade
from utils.permissions import IsOwnerOrReadOnly


class UsuarioWriteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    foto = serializers.ImageField(required=False)
    totalEventos = serializers.IntegerField(required=False)
    criador = serializers.BooleanField(required=False)
    
    class Meta:
        model = Usuario
        exclude = ['password', 'is_superuser', 'is_staff']
        read_only_fields = ['last_login', 'data_joined']

    def update(self, instance, validated_data):
        if 'esportePreferido' in validated_data and validated_data['esportePreferido'] != instance.esportePreferido:
            novo_esporte_preferido = validated_data['esportePreferido']

            # Conta as atividades do usuário com o novo esporte preferido
            nova_quantidade_atividades = Atividade.objects.filter(
                usuario=instance,
                evento__esporte=novo_esporte_preferido
            ).count()

            instance.totalEventos = nova_quantidade_atividades

        return super().update(instance, validated_data)


class UsuarioReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        exclude = ['password', 'is_superuser', 'is_staff']

    def get_foto(self, instance):
        # Verifica se a foto não é nula antes de retornar o URL
        if instance.foto:
            return self.context['request'].build_absolute_uri(instance.foto.url)
        else:
            return None

    def to_representation(self, instance):
        # Obtém o usuário autenticado
        user = self.context['request'].user

        # Se o usuário autenticado é o mesmo que o perfil sendo serializado,
        # permita o acesso a todos os campos
        if instance == user:
            return super().to_representation(instance)
        
        # Caso contrário, permita o acesso apenas a alguns campos
        return {
            'id': instance.id,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'username': instance.username,
            'esportePreferido': instance.esportePreferido,
            'totalEventos': instance.totalEventos,
            'foto': self.get_foto(instance),
        }


class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all() 
    serializer_class = UsuarioReadSerializer
    parser_classes = [MultiPartParser, FormParser]
    renderer_classes = [JSONRenderer, MultiPartRenderer]
    permission_classes = [IsOwnerOrReadOnly]
    # a criação deve ser feita pelo endpoint de registro e não será possível excluir, apenas inativar
    http_method_names = ['get', 'put']  

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return super().get_serializer_class()
        return UsuarioWriteSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

class CustomUserDetailsSerializer(UserDetailsSerializer):
    # Adicione os campos extras aqui
    esportePreferido = serializers.CharField(max_length=255, allow_null=True, required = False)
    cpf = serializers.CharField(max_length=14, allow_null=True, required = False)
    cep = serializers.CharField(max_length=9, allow_null=True,  required = False)
    endereco = serializers.CharField(max_length=255, allow_null=True,  required = False)
    cidade =  serializers.CharField(max_length=255, allow_null=True,  required = False)
    estado =  serializers.CharField(max_length=255, allow_null=True,  required = False)
    foto = serializers.ImageField(allow_null=True,  required = False)
    totalEventos = serializers.IntegerField(allow_null=True, required = False)
    criador = serializers.BooleanField(allow_null=True, required = False)
    representa = serializers.CharField(allow_null=True, required = False)

    class Meta(UserDetailsSerializer.Meta):
        extra_fields = UserDetailsSerializer.Meta.extra_fields + ['esportePreferido', 'cpf', 'cep', 'endereco', 'cidade', 'estado','foto', 'totalEventos', 'criador', 'representa', 'quer_criar']
        fields = ('pk', *extra_fields)



from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from utils.validators import valida_cpf, valida_estado

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    esportePreferido = serializers.CharField(max_length=30)
    cpf = serializers.CharField(max_length=30)
    cep = serializers.CharField(max_length=30)
    endereco = serializers.CharField(max_length=255)
    cidade = serializers.CharField(max_length=255)
    estado = serializers.CharField(max_length=2)
    quer_criar = serializers.BooleanField(required=True)
    representa = serializers.CharField(max_length=255, required=False)

    def validate_cpf(self, value):
        if not valida_cpf(value):
            raise serializers.ValidationError('CPF inválido.')
        return value

    def validate_estado(self, value):
        if not valida_estado(value):
            raise serializers.ValidationError('Estado inválido.')
        return value

    def custom_signup(self, request, user):
        
        user.cep = self.validated_data.get('cep', '')
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.cpf = self.validated_data.get('cpf', '')
        user.endereco = self.validated_data.get('endereco', '')
        user.estado = self.validated_data.get('estado', '')
        user.cidade = self.validated_data.get('cidade', '')
        user.esportePreferido = self.validated_data.get('esportePreferido', '')
        user.representa = self.validated_data.get('representa', '')
        user.quer_criar = self.validated_data.get('quer_criar', '')
        user.save()


    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            **super().get_cleaned_data(),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'cep': self.validated_data.get('cep', ''),
            'cpf': self.validated_data.get('cpf', ''),
            'endereco': self.validated_data.get('endereco', ''),
            'estado': self.validated_data.get('estado', ''),
            'cidade': self.validated_data.get('cidade', ''),
            'representa': self.validated_data.get('representa', ''),
            'quer_criar': self.validated_data.get('quer_criar', '')
        }

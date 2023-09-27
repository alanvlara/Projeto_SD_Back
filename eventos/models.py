from django.db import models
from django.utils import timezone
from pytz import timezone as pytz_timezone
from rest_framework import serializers

from usuario.models import Usuario

brasilia_timezone = pytz_timezone('America/Sao_Paulo')

class Evento(models.Model):
    # o id é gerado automaticamente
    titulo = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    data = models.DateField()
    esporte = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, blank=True, null=True, on_delete=models.CASCADE)
    qr_code = models.URLField(null=True, blank=True)
    representa = models.CharField(max_length=255, null=True, blank=True)

    def delete(self, *args, **kwargs):
        data_evento = self.data
        data_atual_brasilia = timezone.now().astimezone(brasilia_timezone).date()

        # Verificar se a data é menor que a data atual em Brasília
        if data_evento > data_atual_brasilia:
            super().delete(*args, **kwargs)
        else:
            raise serializers.ValidationError("Você não pode excluir eventos passados ou que sejam hoje.")

    def __str__(self) -> str:
        return self.titulo
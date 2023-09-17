from django.db import models
from django.core.exceptions import ValidationError

from usuario.models import Usuario

# Create your models here.
class Evento(models.Model):
    # o id é gerado automaticamente
    titulo = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    data = models.DateField()
    esporte = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, blank=True, null=True, on_delete=models.CASCADE)
    qr_code = models.URLField(null=True, blank=True)
    representa = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo
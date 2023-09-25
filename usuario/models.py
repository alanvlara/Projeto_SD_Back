from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


def get_upload_path_usuario(instance, filename):
    if not instance.id:
        return f'usuarios/temp/{filename}'
    return f'usuarios/{instance.id}/{filename}'

class Usuario(AbstractUser):
    esportePreferido = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    cidade =  models.CharField(max_length=255, null=True, blank=True)
    estado =  models.CharField(max_length=255, null=True, blank=True)
    foto = models.ImageField(upload_to=get_upload_path_usuario, null=True, blank=True, default='padroes/default-user.jpg')
    totalEventos = models.IntegerField(default=0, null=True, blank=True)
    quer_criar = models.BooleanField(null=True, blank=True, default=False)
    criador = models.BooleanField(null=True, blank=True, default=False)
    representa = models.CharField(max_length=255, null=True, blank=True, default="Nenhuma")
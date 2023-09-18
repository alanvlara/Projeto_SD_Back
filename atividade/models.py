from django.db import models

from usuario.models import Usuario
from eventos.models import Evento
from utils.storages import PrivateMediaStorage


def get_upload_path_atividade(instance, filename):
    if not instance.id:
        return f'atividades/temp/{filename}'
    return f'atividades/{instance.id}/{filename}'

# Create your models here.
class Atividade(models.Model):
    # o id é gerado automaticamente
    usuario = models.ForeignKey(Usuario, related_name='atividade_usuario', on_delete=models.CASCADE, null=True)
    data = models.DateField(auto_now_add=True)
    # storage=PrivateMediaStorage() add na imagem se quiser que ela seja privada
    foto = models.ImageField(upload_to=get_upload_path_atividade, null=True, blank=True, default='padroes/atividade-default.jpg')
    evento = models.ForeignKey(Evento, null=True, blank=True, on_delete=models.CASCADE)


    def delete(self, using=None, keep_parents=False):
        if self.evento and self.evento.esporte and self.usuario:
            usuario = self.usuario
            evento_esporte = self.evento.esporte

            if (
                usuario.esportePreferido == evento_esporte
                and hasattr(usuario, "totalEventos")
                and usuario.totalEventos > 0
            ):
                usuario.totalEventos -= 1
                usuario.save()

        super(Atividade, self).delete(using=using, keep_parents=keep_parents)

    # def __str__(self) -> str:
    #     return self.data
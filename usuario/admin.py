from django.contrib import admin

from usuario.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    # campos que vão aparecer na listagem
    list_display = ('id', 'username')
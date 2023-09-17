from django.contrib import admin

from eventos.models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    # campos que vão aparecer na listagem
    list_display = ('id', 'titulo', 'link', 'data', 'esporte')
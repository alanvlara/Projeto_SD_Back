from django.contrib import admin

from atividade.models import Atividade

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    # campos que vão aparecer na listagem
    list_display = ('id', 'usuario', 'evento')
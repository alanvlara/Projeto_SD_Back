from django.urls import path, include
from rest_framework import routers

from atividade.views import AtividadeView
from utils import gerar_certificado_view


router = routers.DefaultRouter()
router.register('atividades', AtividadeView)  

urlpatterns = [
    path('', include(router.urls)),
    path('gerar_certificado/<int:atividade_id>/', gerar_certificado_view.gerar_certificado, name='gerar_certificado'),
]
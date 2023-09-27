from django.urls import path, include
from rest_framework import routers

from eventos.views import EventoView
from utils import exportar_excel_view


router = routers.DefaultRouter()
router.register('eventos', EventoView)  

urlpatterns = [
    path('', include(router.urls)),
    path('exportar_excel/<int:evento_id>/', exportar_excel_view.ExportarDadosParaExcel.as_view(), name='exportar_excel'),
]
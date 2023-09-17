from django.urls import path, include
from rest_framework import routers

from eventos.views import EventoView


router = routers.DefaultRouter()
router.register('eventos', EventoView)  

urlpatterns = [
    path('', include(router.urls)),
]
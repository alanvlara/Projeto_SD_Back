from django.urls import path, include
from rest_framework import routers

from usuario.views import UsuarioView


router = routers.DefaultRouter()
router.register('usuarios', UsuarioView)  

urlpatterns = [
    path('', include(router.urls)),
]
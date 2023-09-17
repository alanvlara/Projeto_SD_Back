
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions, routers
from drf_yasg import openapi  
from drf_yasg.views import get_schema_view  
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.views import PasswordResetConfirmView
from utils.custom_view import CustomUserDetailsView
from utils.custom_view_register import CustomRegisterView

router = routers.DefaultRouter()
schema_view = get_schema_view(
    openapi.Info(
        title='DesporPato API',
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('atividade/', include('atividade.urls')),
    path('evento/', include('eventos.urls')),
    path('api/swagger.<slug:format>)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/user/', CustomUserDetailsView.as_view(), name='custom_user_details'),
    path('accounts/registration/', CustomRegisterView.as_view(), name='custom_register'),
    path('accounts/', include('dj_rest_auth.urls')),
    path(
        'api/accounts/password/reset/confirm/<str:uidb64>/<str:token>',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

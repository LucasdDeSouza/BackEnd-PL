from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static
from core.views import UserViewSet
from core.views import PropriedadeViewSet
from core.views import ProprietarioViewSet
from core.views import UsuarioViewSet
from core.views import CorretorViewSet
from uploader.router import router as uploader_router

router = DefaultRouter()
router.register(r"Propriedades", PropriedadeViewSet)
router.register(r"Proprietarios", ProprietarioViewSet)
router.register(r"Usuarios", UsuarioViewSet)
router.register(r"Corretor", CorretorViewSet)
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
      path('api/media/', include(uploader_router.urls)),  # nova linha
    # API
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)


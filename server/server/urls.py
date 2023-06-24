"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


from core.views import WalletViewSet

router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallet')

urlpatterns = [
    path(f"{settings.API_VERSION_PREFIX.strip('/')}/", include(router.urls)),
    path("admin/", admin.site.urls),

    path(f"{settings.API_VERSION_PREFIX.strip('/')}/schema/", SpectacularAPIView.as_view(), name='schema'),
    path(f"{settings.API_VERSION_PREFIX.strip('/')}/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(f"{settings.API_VERSION_PREFIX.strip('/')}/schema/redoc/", SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

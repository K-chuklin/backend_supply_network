from django.urls import include, path
from rest_framework.routers import DefaultRouter
from providers.views.views import ProviderViewSet
from providers.apps import ProvidersConfig

app_name = ProvidersConfig.name

providers_router = DefaultRouter()
providers_router.register(r'providers', ProviderViewSet, basename='providers')

urlpatterns = [
    path('', include(providers_router.urls)),
]

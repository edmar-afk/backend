from rest_framework.routers import DefaultRouter
from api.urls import api_router
from django.urls import path, include

router = DefaultRouter()

router.registry.extend(api_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, ItemViewSet)

v1_router = DefaultRouter()
v1_router.register('categories', CategoryViewSet, basename='categories')
v1_router.register('items', ItemViewSet, basename='items')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(v1_router.urls)),
]

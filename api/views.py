from rest_framework import filters, mixins, viewsets
from django_filters import rest_framework

from api.models import Category, Item
from api.serializers import CategorySerializer, ItemSerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'slug'
    search_fields = ('name',)


class ItemViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (filters.SearchFilter,
                       rest_framework.DjangoFilterBackend)
    search_fields = ('name',)
    filterset_fields = ('category',)

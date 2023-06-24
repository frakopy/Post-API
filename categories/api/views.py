from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permisions import IsAdminOrReadonly
from django_filters.rest_framework import DjangoFilterBackend

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadonly]
    serializer_class = CategorySerializer
    queryset =  Category.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
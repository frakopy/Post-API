from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from .serializer import PostSerializer
from .permisions import IsAdminOrReadonly
from django_filters.rest_framework import DjangoFilterBackend

class PostApiViewSet(ModelViewSet):
    permission_classes= [IsAdminOrReadonly]
    serializer_class = PostSerializer
    queryset =  Post.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends =  [DjangoFilterBackend]
    filterset_fields = ['category__slug']
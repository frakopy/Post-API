from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CommentsSerializer
from .permisions import IsOwnerOrReadAndCreateOnly

class CommentsApiModelViewset(ModelViewSet):
    """
    Take note that ordering also can be easily handled in 
    django model simply adding ordering = ['-created'] to Meta subclass, so
    you do not need to user filter_backends=[OrderingFilter] and ordering= ['-created']
    in this view
    """
    serializer_class = CommentsSerializer
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['post']
    ordering = ['-created']
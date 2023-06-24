from rest_framework.routers import DefaultRouter
from .views import CommentsApiModelViewset

router_comment = DefaultRouter()

router_comment.register(prefix='comments', basename='comments', viewset=CommentsApiModelViewset)
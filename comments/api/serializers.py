from rest_framework.serializers import ModelSerializer
from comments.models import Comment


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'created', 'user', 'post']
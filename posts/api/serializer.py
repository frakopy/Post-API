from rest_framework import serializers
from posts.models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user =  UserSerializer(required=False)
    # user = serializers.StringRelatedField()
    category =  CategorySerializer(required=False)
    class Meta:
        model = Post
        fields = ["title", "content", "slug", "miniature", "created", "published", "user", "category"]
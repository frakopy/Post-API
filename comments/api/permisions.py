from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            comment_id = view.kwargs['pk']
            comment =  Comment.objects.get(id=comment_id)

            request_user_id = request.user.id
            comment_user_id = comment.user_id

            if request_user_id == comment_user_id:
                return True
            
            return False             
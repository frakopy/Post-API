from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):

    # Display specific columns to show in the panel
    list_display = ("comment", "created", "user", "post")


admin.site.register(Comment, CommentAdmin)


from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):

    # Display specific columns to show in the panel
    list_display = ("title", "content", "user", "category", "published", "created")

admin.site.register(Post, PostAdmin)

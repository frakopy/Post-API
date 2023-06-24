from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):

    # Display specific columns to show in the panel
    list_display = ("title", "published")


admin.site.register(Category, CategoryAdmin)


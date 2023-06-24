from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from categories.api.router import router_categories
from posts.api.router import router_posts
from comments.api.routers import router_comment

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Blog API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="frako789@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    #Paths for swagger
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #Pahts for API
    path('api/', include('users.api.router')),
    path('api/', include(router_categories.urls)),
    path('api/', include(router_posts.urls)),
    path('api/', include(router_comment.urls)),
]

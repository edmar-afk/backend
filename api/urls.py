from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CommentViewSet

# Create a router instance
api_router = DefaultRouter()

# Register ProductViewSet
api_router.register(r'products', ProductViewSet)

# Register CommentViewSet
api_router.register(r'comments', CommentViewSet)

# Optionally, you can append this router's URLs to an existing urlpatterns list
urlpatterns = [
    # Your existing paths can go here if needed
    path('', include(api_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# Append the router's URLs to urlpatterns
urlpatterns += api_router.urls

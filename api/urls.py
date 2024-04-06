from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CommentViewSet, VisitViewSet, LikeViewSet

# Create a router instance
api_router = DefaultRouter()


api_router.register(r'products', ProductViewSet, basename='products')
api_router.register(r'comments', CommentViewSet, basename='comments')
api_router.register(r'visits', VisitViewSet, basename='visits')
api_router.register(r'likes', LikeViewSet, basename='likes')
# Optionally, you can append this router's URLs to an existing urlpatterns list
urlpatterns = [
    # Your existing paths can go here if needed
    path('', include(api_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Append the router's URLs to urlpatterns
urlpatterns += api_router.urls

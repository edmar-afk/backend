from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CommentViewSet, VisitViewSet, LikeViewSet, ChatbotViewSet

# Create a router instance
api_router = DefaultRouter()

api_router.register(r'products', ProductViewSet, basename='products')
api_router.register(r'comments', CommentViewSet, basename='comments')
api_router.register(r'visits', VisitViewSet, basename='visits')
api_router.register(r'likes', LikeViewSet, basename='likes')
api_router.register(r'chatbot', ChatbotViewSet, basename='chatbot')

# Define urlpatterns
urlpatterns = [
    path('', include(api_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('api/chatbot/', ChatbotAPIView.as_view(), name='chatbot_api'),  # Include the chatbot API view here
]

from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, action
from .models import Products, Comments, Visit, Like
from .serializers import ProductSerializer, CommentSerializer, VisitorSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.http import JsonResponse
from django.db.models import Sum
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet): 
    queryset = Products.objects.all() 
    serializer_class = ProductSerializer  
    permission_classes = [AllowAny] 

class CommentViewSet(viewsets.ModelViewSet): 
    queryset = Comments.objects.all() 
    serializer_class = CommentSerializer 
    permission_classes = [AllowAny]
    
class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = [AllowAny]
    
    def create(self, request):
        user_identifier = request.META.get('REMOTE_ADDR')  # Example: Using IP address for identification
        try:
            visit = Visit.objects.get(user_identifier=user_identifier)
            visit.visit_count += 1
            visit.save()
        except Visit.DoesNotExist:
            visit = Visit.objects.create(user_identifier=user_identifier, visit_count=1)
        serializer = VisitorSerializer(visit)
        return Response(serializer.data)



class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [AllowAny]
    
    def create(self, request):
        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key
        ip_address = request.META.get('REMOTE_ADDR')

        # Check if the user has already liked the page
        existing_like = Like.objects.filter(ip_address=ip_address).first()

        if existing_like:
            return Response({'status': 'failure', 'message': 'User already liked the page'})
        else:
            Like.objects.create(ip_address=ip_address)
            return Response({'status': 'success', 'message': 'Page liked'})

    @action(detail=False, methods=['delete'])
    def delete_latest(self, request):
        latest_like = Like.objects.latest('id')  # Assuming id is auto-incrementing
        latest_like.delete()
        return Response(status=204)
    
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
import uuid
from django.core.exceptions import ObjectDoesNotExist
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
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        existing_visit = Visit.objects.filter(ip_address=ip_address, user_agent=user_agent).first()

        if existing_visit:
            return Response({'status': 'failure', 'message': 'User already visited the website'})
        else:
            new_visit = Visit.create(ip_address=ip_address, user_agent=user_agent)
            new_visit.save()
            return Response({'status': 'success', 'message': 'Website visited'})



class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [AllowAny]
    
    def create(self, request):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        existing_like = Like.objects.filter(ip_address=ip_address, user_agent=user_agent).first()

        if existing_like:
            return Response({'status': 'failure', 'message': 'User already liked the page'})
        else:
            new_like = Like.create(ip_address=ip_address, user_agent=user_agent)
            new_like.save()
            return Response({'status': 'success', 'message': 'Page liked'})
        

    @action(detail=False, methods=['delete'])
    def delete_latest(self, request):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        try:
            like_to_delete = Like.objects.filter(ip_address=ip_address, user_agent=user_agent).latest('id')
            like_to_delete.delete()
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({'status': 'failure', 'message': 'No like found to delete'}, status=404)
    
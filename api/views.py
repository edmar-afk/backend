from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from .models import Products, Comments
from .serializers import ProductSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from rest_framework import viewsets


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):  # Defining ProductViewSet class inheriting from ModelViewSet
    queryset = Products.objects.all()  # Setting queryset to retrieve all Products objects
    serializer_class = ProductSerializer  # Setting serializer_class to ProductSerializer
    permission_classes = [AllowAny]  # Setting permission_classes to allow any user access

class CommentViewSet(viewsets.ModelViewSet):  # Defining CommentViewSet class inheriting from ModelViewSet
    queryset = Comments.objects.all()  # Setting queryset to retrieve all Comments objects
    serializer_class = CommentSerializer  # Setting serializer_class to CommentSerializer
    permission_classes = [AllowAny]  # Setting permission_classes to allow any user access


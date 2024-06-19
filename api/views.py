from rest_framework.decorators import action
from .models import Products, Comments, Visit, Like
from .serializers import ProductSerializer, CommentSerializer, VisitorSerializer, LikeSerializer, ChatbotSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
import json
from difflib import get_close_matches
from django.conf import settings
import os
BASE_DIR = settings.BASE_DIR

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
    
    
    
    
    
    
    
    
# Load the knowledge base from a JSON file
def load_knowledge_base(file_path: str):
    full_path = os.path.join(BASE_DIR, file_path)
    with open(full_path, 'r') as file:
        data = json.load(file)
    return data

# Save the updated knowledge base to the JSON file
def save_knowledge_base(file_path: str, data: dict):
    full_path = os.path.join(BASE_DIR, file_path)
    with open(full_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

class ChatbotViewSet(viewsets.ViewSet):
    serializer_class = ChatbotSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_question = serializer.validated_data['question']
            knowledge_base = load_knowledge_base('knowledge_base.json')
            best_match = find_best_match(user_question, [q["question"] for q in knowledge_base["questions"]])

            if best_match:
                answer = get_answer_for_question(best_match, knowledge_base)
                return Response({'answer': answer}, status=status.HTTP_200_OK)
            else:
                return Response({'answer': "I don't understand the question."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
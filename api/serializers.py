from rest_framework.serializers import ModelSerializer
from .models import Products, Comments, Visit, Like

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'stack', 'details', 'status', 'downloads', 'fileName', 'price']

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'name', 'rate', 'comment', 'date']
        
class VisitorSerializer(ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
        
class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
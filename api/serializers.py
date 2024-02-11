from rest_framework.serializers import ModelSerializer
from .models import Products, Comments

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'stack', 'details', 'status', 'downloads', 'fileName', 'price']

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'name', 'rate', 'comment', 'date']
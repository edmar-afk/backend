from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

now = timezone.now()
currentDate = now.date()

class Products(models.Model):
    name = models.CharField(max_length=250)
    stack = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    status = models.CharField(max_length=10)
    downloads = models.IntegerField()
    fileName = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],)
    price = models.IntegerField()
    
    def __str__(self):
        return f'Product - {self.name}'
    
    class Meta:
        verbose_name = "Product"
    
class Comments(models.Model):
    name = models.CharField(max_length=250)
    rate = models.IntegerField()
    comment = models.CharField(max_length=1000)
    date = models.DateField(default=now)
    
    def __str__(self):
        return f'Client - {self.name}'
    
    class Meta:
        verbose_name = "Comment"
        

class Visit(models.Model):
    user_identifier = models.CharField(max_length=100, unique=True)
    visit_count = models.IntegerField(default=0)
    visited_today = models.BooleanField(default=True)
    

class Like(models.Model):
    session_key = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.CharField(max_length=50)
    clicked = models.BooleanField(default=False)
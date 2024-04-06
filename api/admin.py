from django.contrib import admin
from .models import Products, Comments, Visit, Like
# Register your models here.

admin.site.register(Products)
admin.site.register(Comments)
admin.site.register(Visit)
admin.site.register(Like)
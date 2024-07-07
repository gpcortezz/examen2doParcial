from django.contrib.auth import authenticate
from django.contrib.auth.models import User  
from rest_framework import serializers
from .models import *

#user
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_active']
        
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está en uso.")
        return value
    

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

class ToDoIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id']

class ToDoIDTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title']
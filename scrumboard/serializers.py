from rest_framework import serializers
from django.contrib.auth.models import User
from .models import List, Card, Project

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__' 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__' 

class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True,many=True)
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = List
        fields = '__all__' 



class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields='__all__'

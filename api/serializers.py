from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Reference the User model
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Include fields you want to serialize


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'  # Serialize all fields of the Client model


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'  # Serialize all fields of the Project model

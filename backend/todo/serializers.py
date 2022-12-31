"""Serializers for Models in Todo app"""
from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Serializer for Todo model"""

    class Meta:
        model = Todo
        fields = ("id", "title", "description", "completed")

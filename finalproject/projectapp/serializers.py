from django.contrib.auth.models import User
from .models import LearningPath
from rest_framework import serializers

class LearningPathSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearningPath
        fields = ("id", "title", "progress", "date")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
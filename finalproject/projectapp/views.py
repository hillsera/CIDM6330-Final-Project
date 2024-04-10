from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from .models import LearningPath
from projectapp.serializers import UserSerializer, LearningPathSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class LearningPathViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows learning paths to be viewed or edited.
    """
    queryset = LearningPath.objects.all().order_by("date")
    serializer_class = LearningPathSerializer
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from django.urls import reverse

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
    queryset = LearningPath.objects.all().order_by("title")
    serializer_class = LearningPathSerializer

    def get_learningpath_list_url(self):
        """
        Helper method to get the URL for the list action of the LearningPathViewSet.
        """
        return reverse('projectapp:learningpath-list')
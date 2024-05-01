from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework import routers
from rest_framework.test import APIRequestFactory, APITestCase

from .models import LearningPath

# Create your tests here.
class LearningPathAPITest(APITestCase):
    def setUp(self):
        self.learning_path_data = {
            'id': 1,
            'title': 'Test Learning Path',
            'duration': 300,
            'progress': 0,
        }

        self.list_url = reverse('projectapp:learningpath-list')

    def test_add_learning_path(self):
        response = self.client.post(self.list_url, data=self.learning_path_data, format='json')

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Retrieve the learning path from the database
        learning_path = LearningPath.objects.get(id=self.learning_path_data['id'])

        # Assert that the learning path is added correctly
        learning_path = LearningPath.objects.get(id=self.learning_path_data['id'])
        self.assertEqual(learning_path.title, self.learning_path_data['title'])
        self.assertEqual(learning_path.duration, self.learning_path_data['duration'])
        self.assertEqual(learning_path.progress, self.learning_path_data['progress'])

    
    
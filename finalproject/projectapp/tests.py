from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework import routers
from rest_framework.test import APIRequestFactory, APITestCase

from .models import LearningPath

# Create your tests here.
class LearningPathAPITest(APITestCase):
    def test_add_learning_path(self):
        # Prepare test data
        learning_path_data = {
            'id': 1,
            'title': 'Test Learning Path',
            'duration': 300,  # Duration in seconds
            'progress': 0,
        }

        # Send POST request to add a learning path
        url = reverse('projectapp:learningpath-list')  # Assuming you have a URL named 'learning-path-list' for adding learning paths
        response = self.client.post(url, data=learning_path_data, format='json')

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Retrieve the learning path from the database
        learning_path = LearningPath.objects.get(id=learning_path_data['id'])

        # Assert that the learning path is added correctly
        learning_path = LearningPath.objects.get(id=learning_path_data['id'])
        self.assertEqual(learning_path.title, learning_path_data['title'])
        self.assertEqual(learning_path.duration, learning_path_data['duration'])
        self.assertEqual(learning_path.progress, learning_path_data['progress'])

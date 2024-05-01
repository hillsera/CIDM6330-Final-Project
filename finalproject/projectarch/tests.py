from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime

from projectapp.models import LearningPath
from projectarch.domain.model import DomainLearningPath
from projectarch.services.commands import (
    AddPathCommand,
    ListLearningPathCommand
)
import os
import csv
from unittest.mock import patch

class TestCommands(TestCase):
    def setUp(self):

        self.domain_path_1 = DomainLearningPath(
            id=1,
            title="Learning Video 1",
            duration=60,
            progress=0,
        )

        self.domain_path_2 = DomainLearningPath(
            id=2,
            title="Learning Video 2",
            duration=360,
            progress=0,
        )

    def test_command_add(self):
        add_command = AddPathCommand()
        add_command.execute(self.domain_path_1)

        self.assertEqual(LearningPath.objects.count(), 1)
        self.assertEqual(LearningPath.objects.get(id=1).title, self.domain_path_1.title)

    def test_command_list_learning_path(self):
        add_command = AddPathCommand()
        add_command.execute(self.domain_path_1)
        add_command.execute(self.domain_path_2)

        list_command = ListLearningPathCommand()
        result = list_command.execute()

        self.assertEqual(len(result), 2)

class TestDomainLearningPath(TestCase):
    def test_watch_updates_progress(self):
        # Create a DomainLearningPath instance for testing
        learning_path = DomainLearningPath(id=1, title="Test Learning Path", duration=3, progress=0)

        # Call the watch method
        learning_path.watch()

        # Check if the progress is updated correctly
        self.assertLessEqual(learning_path.progress, learning_path.duration)



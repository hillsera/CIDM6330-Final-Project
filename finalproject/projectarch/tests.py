from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime

from projectapp.models import LearningPath
from projectarch.domain.model import DomainLearningPath
from projectarch.services.commands import (
    AddPathCommand,
    ListLearningPathCommand,
    SaveLearningPathProgressCommand,
    ChangeLearningPathCommand
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

class TestSaveProgressCommand(TestCase):
    def setUp(self):
        # Create a DomainLearningPath instance for testing
        self.domain_path = DomainLearningPath(
            id=1,
            title="Test Learning Path",
            duration=10,
            progress=0,
        )

        # Create a LearningPath instance in the database for testing
        LearningPath.objects.create(
            id=self.domain_path.id,
            title=self.domain_path.title,
            duration=self.domain_path.duration,
        )

    def test_save_progress(self):
        # Create an instance of the SaveProgressCommand
        save_progress_command = SaveLearningPathProgressCommand()

        # Execute the command to save progress
        progress = 5
        save_progress_command.execute(self.domain_path, progress)

        # Retrieve the LearningPath instance from the database
        learning_path = LearningPath.objects.get(id=self.domain_path.id)

        # Assert that the progress has been correctly updated
        self.assertEqual(learning_path.progress, progress)

    def test_save_progress_nonexistent_learning_path(self):
        # Create an instance of the SaveProgressCommand
        save_progress_command = SaveLearningPathProgressCommand()

        # Attempt to save progress for a non-existent learning path
        non_existent_path = DomainLearningPath(
            id=100,  # Assuming ID 100 doesn't exist in the database
            title="Non-existent Path",
            duration=5,
            progress=0,
        )
        progress = 3

        # Check that executing the command raises a ValueError
        with self.assertRaises(ValueError):
            save_progress_command.execute(non_existent_path, progress)

class TestChangePathCommand(TestCase):
    def setUp(self):
        # Create a DomainLearningPath instance for testing
        self.domain_path = DomainLearningPath(
            id=1,
            title="Test Learning Path",
            duration=10,
            progress=0,
        )

        # Create a LearningPath instance in the database for testing
        LearningPath.objects.create(
            id=self.domain_path.id,
            title=self.domain_path.title,
            duration=self.domain_path.duration,
        )

    def test_change_path(self):
        # Create an instance of the ChangePathCommand
        change_path_command = ChangeLearningPathCommand()

        # Execute the command to change properties
        new_title = "Updated Learning Path"
        new_duration = 15
        change_path_command.execute(self.domain_path, new_title, new_duration)

        # Retrieve the updated LearningPath instance from the database
        learning_path = LearningPath.objects.get(id=self.domain_path.id)

        # Assert that the properties have been correctly updated
        self.assertEqual(learning_path.title, new_title)
        self.assertEqual(learning_path.duration, new_duration)

    def test_change_path_nonexistent_learning_path(self):
        # Create an instance of the ChangePathCommand
        change_path_command = ChangeLearningPathCommand()

        # Attempt to change properties for a non-existent learning path
        non_existent_path = DomainLearningPath(
            id=100,  # Assuming ID 100 doesn't exist in the database
            title="Non-existent Path",
            duration=5,
            progress=0,
        )
        new_title = "Updated Title"
        new_duration = 10

        # Check that executing the command raises a ValueError
        with self.assertRaises(ValueError):
            change_path_command.execute(non_existent_path, new_title, new_duration)


class TestDomainLearningPath(TestCase):
    def test_watch_updates_progress(self):
        # Create a DomainLearningPath instance for testing
        learning_path = DomainLearningPath(id=1, title="Test Learning Path", duration=3, progress=0)

        # Call the watch method
        learning_path.watch()

        # Check if the progress is updated correctly
        self.assertLessEqual(learning_path.progress, learning_path.duration)



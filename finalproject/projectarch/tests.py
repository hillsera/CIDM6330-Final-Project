from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime

from projectapp.models import LearningPath
from projectarch.domain.model import DomainLearningPath
from projectarch.services.commands import (
    AddPathCommand
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

    def test_command_add(self):
        add_command = AddPathCommand()
        add_command.execute(self.domain_path_1)

        self.assertEqual(LearningPath.objects.count(), 1)
        self.assertEqual(LearningPath.objects.get(id=1).title, self.domain_path_1.title)
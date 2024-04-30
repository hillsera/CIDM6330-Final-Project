"""
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
"""
import sys
from abc import ABC, abstractmethod
from datetime import datetime
from injector import Injector, inject
import pytz

import requests
from django.db import transaction

from finalproject.projectapp.models import LearningPath
from projectarch.domain.model import DomainLearningPath


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("A command must implement the execute method")
    
class PythonTimeStampProvider:
    def __init__(self):
        self.now = datetime.now(pytz.UTC).isoformat()


class AddPathCommand(Command):
    """
    Adding a learning path
    """

    @inject
    def __init__(self, now: PythonTimeStampProvider = PythonTimeStampProvider()):
        self.now = now

    def execute(self, data: DomainLearningPath, timestamp=None):
        learningpath = LearningPath(data.id, data.title, data.duration)
        learningpath.timestamp = self.now

        with transaction.atomic():
            learningpath.save()



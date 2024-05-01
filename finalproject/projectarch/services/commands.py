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

from projectapp.models import LearningPath
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

    def execute(self, data: DomainLearningPath):
        learningpath = LearningPath(data.id, data.title, data.duration)

        with transaction.atomic():
            learningpath.save()

class ListLearningPathCommand(Command):
    """
    swapping in Django ORM for the database manager
    """

    def __init__(self, order_by="id"):
        self.order_by = order_by

    def execute(self):
        return LearningPath.objects.all().order_by(self.order_by)
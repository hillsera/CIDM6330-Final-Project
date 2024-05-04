import sys
from abc import ABC, abstractmethod
from datetime import datetime
import pytz
from injector import Injector, inject

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

    def execute(self, data: DomainLearningPath, timestamp=None):
        learningpath = LearningPath(data.id, data.title, data.duration, timestamp)
        learningpath.timestamp = self.now

        with transaction.atomic():
            learningpath.save()


class ListLearningPathCommand(Command):
    """
    Swapping in Django ORM for the database manager
    """

    def __init__(self, order_by="id"):
        self.order_by = order_by

    def execute(self):
        return LearningPath.objects.all().order_by(self.order_by)
    

class SaveLearningPathProgressCommand(Command):
    """
    Command to save progress for a learning path
    """

    @transaction.atomic
    def execute(self, data: DomainLearningPath, progress: int):
        try:
            learning_path = LearningPath.objects.get(id=data.id)
        except LearningPath.DoesNotExist:
            raise ValueError(f"Learning path with id {data.id} does not exist")

        learning_path.progress = progress
        learning_path.save()

class ChangeLearningPathCommand(Command):
    """
    Command to change to a new learning path
    """

    @transaction.atomic
    def execute(self, data: DomainLearningPath, new_title: str, new_duration: int):
        try:
            learning_path = LearningPath.objects.get(id=data.id)
        except LearningPath.DoesNotExist:
            raise ValueError(f"Learning path with id {data.id} does not exist")

        learning_path.title = new_title
        learning_path.duration = new_duration
        learning_path.save()

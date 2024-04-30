from django.db import models
from tqdm import tqdm
import time

from projectarch.domain.model import DomainLearningPath

class LearningPath(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=300)
    duration = models.IntegerField()
    progress = models.IntegerField(default=0)  # Add progress field

    def __str__(self):
        return f"{self.title}"

    def watch_video(self):  # Renamed method
        with tqdm(total=self.duration, desc=f"Watching '{self.title}'", unit="s") as pbar:
            start_time = time.time()
            while True:
                elapsed_time = time.time() - start_time
                if elapsed_time >= self.duration:
                    break
                time.sleep(1)  # Simulate watching video for 1 second
                self.progress = min(int(elapsed_time), self.duration)  # Update progress
                pbar.update(1)

    class Meta:
        app_label = "projectapp"

    @staticmethod
    def update_from_domain(domain_learning_path: DomainLearningPath):
        try:
            learningpath = LearningPath.objects.get(id=domain_learning_path.id)
        except LearningPath.DoesNotExist:
            learningpath = LearningPath(id=domain_learning_path.id)

        learningpath.title = domain_learning_path.title
        learningpath.duration = domain_learning_path.duration

        learningpath.save()

    def to_domain(self) -> DomainLearningPath:
        return DomainLearningPath(
            id=self.id,
            title=self.title,
            duration=self.duration,
            progress=self.progress
        )

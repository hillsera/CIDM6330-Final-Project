from datetime import date
from tqdm import tqdm
import time


class DomainLearningPath:
    """
    LearningPath domain model.
    """

    def __init__(self, id, title, duration, progress):
        self.id = id
        self.title = title
        self.duration = duration
        self.progress = progress

    def watch(self):
        with tqdm(total=self.duration, desc=f"Watching '{self.title}'", unit="s") as pbar:
            start_time = time.time()
            while True:
                elapsed_time = time.time() - start_time
                if elapsed_time >= self.duration:
                    break
                time.sleep(1)  # Simulate watching video for 1 second
                self.progress = min(elapsed_time, self.duration)  # Update progress
                pbar.update(1)


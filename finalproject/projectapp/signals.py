import csv
from pathlib import Path

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.core.files import File
from django.db.models.signals import post_save

from .models import LearningPath

channel_layer = get_channel_layer()


def log_learning_path_to_csv(sender, instance, **kwargs):
    print("Learning Path signal: CSV")

    file = Path(__file__).parent.parent / "projectarch" / "domain" / "created_log.csv"
    print(f"Writing to {file}")

    with open(file, "a+", newline="") as csvfile:
        logfile = File(csvfile)
        logwriter = csv.writer(
            logfile,
            delimiter=",",
        )
        is_empty = csvfile.tell() == 0

        if is_empty:
            logwriter.writerow(['id', 'title', 'duration', 'progress'])

        logwriter.writerow(
            [
                instance.id,
                instance.title,
                instance.duration,
                instance.progress,
            ]
        )

def send_learning_path_to_channel(sender, instance, **kwargs):
    print("Learning Path signal: Channel")
    print(f"Sending learning path to channel: {instance}")

    async_to_sync(channel_layer.send)(
        "learning-path-add", {"type": "print.learningpath", "data": instance.title}
    )


# connect the signal to this receiver
post_save.connect(log_learning_path_to_csv, sender=LearningPath)
post_save.connect(send_learning_path_to_channel, sender=LearningPath)

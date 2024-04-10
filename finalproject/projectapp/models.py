from django.db import models

# Create your models here.
class LearningPath(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=300)
    progress = models.TimeField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
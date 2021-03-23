from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.description

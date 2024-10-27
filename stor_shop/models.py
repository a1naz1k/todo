from django.db import models

# Create your models here.
from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_name

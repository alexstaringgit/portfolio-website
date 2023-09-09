from typing import Any
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField("Project description", default="")
    link = models.CharField(max_length=200, default="")
    tasks = models.TextField("Challenges of that project", default="")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return "Project: " + self.title
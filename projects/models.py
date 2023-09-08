from typing import Any
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    points = models.PositiveIntegerField(default=0)

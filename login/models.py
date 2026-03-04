from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_no = models.CharField(max_length=30, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username
from django.db import models
from .managers import CustomManager

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.FloatField(max_length=20)
    class_room = models.CharField(max_length=20)

    # students = models.Manager()
    students = CustomManager()

    def __str__(self):
        return self.name

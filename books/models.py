from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    image = models.ImageField(upload_to='books/', blank=True, null=True)
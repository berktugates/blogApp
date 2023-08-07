from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=100)    
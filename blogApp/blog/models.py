from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique= True, db_index= True,)

    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog")
    description = RichTextField()
    author = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(unique= True, db_index= True,)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"

class TopWeek(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog")
    description = RichTextField()
    is_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_week = models.BooleanField(default=False)
    slug = models.SlugField(null=False,unique= True, db_index= True,)
    author = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.title}"


class Softwarelang(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="discovery")
    description = RichTextField()
    is_active= models.BooleanField(default=False)
    is_discovery = models.BooleanField(default=False)
    slug = models.SlugField(null=False,unique= True, db_index= True,)
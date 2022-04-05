import datetime

import django
from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, blank=False)
    thumbnail = models.ImageField(upload_to='media/thumbnails')
    position = models.IntegerField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='media/thumbnails')
    price = models.IntegerField()
    url = models.URLField()

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='media/thumbnails')
    pub_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    product = models.ManyToManyField(Product)
    article = models.ManyToManyField(Article)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class Comment(models.Model):
    product = models.ManyToManyField(Product)
    article = models.ManyToManyField(Article)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=150)
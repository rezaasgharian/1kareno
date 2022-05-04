from django.db import models
from django.conf import settings
from django.utils import timezone
from django.conf import settings
from PIL import Image


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
    CATEGORY_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Publish'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='media/thumbnails')
    pub_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    status = models.CharField(choices=CATEGORY_CHOICES, max_length=1)

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.thumbnail.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.thumbnail.path)

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

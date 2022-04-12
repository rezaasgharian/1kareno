from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     biography = models.TextField(null=False, blank=True)
#     phone = models.CharField(max_length=11)
#     avatar = models.ImageField(upload_to='media/avatars', null=True, blank=True)
#
#     def __str__(self):
#         return self.user.first_name
#
#
# def save_profile_user(sender, **kwargs):
#     if kwargs['created']:
#         profile_user = Profile(user=kwargs['instance'])
#         profile_user.save()
#
# post_save.connect(save_profile_user, sender=User)







# from PIL import Image
#
# # resizing images
# def save(self, *args, **kwargs):
#     super().save()
#
#     img = Image.open(self.avatar.path)
#
#     if img.height > 100 or img.width > 100:
#         new_img = (100, 100)
#         img.thumbnail(new_img)
#         img.save(self.avatar.path)

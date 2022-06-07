from django.db import models
from django.db.models.signals import post_save
from django.conf import settings


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    biography = models.TextField(null=False, blank=True)
    phone = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='media/avatars', null=True, blank=True)

    def __str__(self):
        return self.user.first_name
#
#
# def save_profile_user(sender, **kwargs):
#     if kwargs['created']:
#         profile_user = Profile(user=kwargs['instance'])
#         profile_user.save()
#
# post_save.connect(save_profile_user, sender=settings.AUTH_USER_MODEL)
#




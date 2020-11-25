from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

User._meta.get_field('email')._unique = True

class Profile(models.Model):
    User._meta.get_field('email')._unique = True
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isBlocked = models.BooleanField(default=False)
    profile_pic = models.ImageField(default = 'noimage.jpg')

    def __str__(self) -> str:
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Forgot(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(blank=False)
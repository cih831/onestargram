from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=10, blank=True)
    introduce = models.CharField(max_length=200)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
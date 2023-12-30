from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    '''Minimal auth moodel for future expanding'''
    full_name = models.CharField(max_length=200)


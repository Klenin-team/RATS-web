import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    '''Minimal auth moodel for future expanding'''
    id = models.UUIDField(primary_key = True, 
         default = uuid.uuid4, editable = False) 
    full_name = models.CharField(max_length=200)


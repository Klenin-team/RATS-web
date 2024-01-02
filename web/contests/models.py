import uuid
from django.db import models

from problems.models import Problems

class Contests(models.Model):
    id = models.UUIDField(primary_key = True, 
         default = uuid.uuid4, editable = False) 
    title = models.CharField(max_length=300)
    description = models.TextField()
    problems = models.ManyToManyField(Problems)
    

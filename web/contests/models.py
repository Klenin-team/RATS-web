from django.db import models

from problems.models import Problems

class Contests(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    problems = models.ManyToManyField(Problems)
    

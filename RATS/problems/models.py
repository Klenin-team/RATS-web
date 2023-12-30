from django.db import models
from django.utils import choices

from RATS.settings import SUPPORTED_LANGUAGES
from profiles.models import Users


class Problems(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    input_file = models.CharField(max_length=50)
    output_file = models.CharField(max_length=50)


class Tests(models.Model):
    input = models.TextField()
    output = models.TextField()
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)


class Solves(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.CharField(max_length=30, choices=SUPPORTED_LANGUAGES)
    code = models.TextField()

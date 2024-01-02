from django.db import models

from RATS.settings import SUPPORTED_LANGUAGES
from profiles.models import Users


class Problems(models.Model):
    title = models.CharField(max_length=300)
    memory_limitation = models.IntegerField() #Bytes
    time_limitation = models.IntegerField() #Miliseconds
    text = models.TextField()
    input_file = models.CharField(max_length=50)
    output_file = models.CharField(max_length=50)


class Tests(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)


class TestVerdicts(models.Model):
    #Sorry. This is the clothest thing to enum i found
    class Verdicts(models.IntegerChoices):
        OK = 0, ('Done')
        WA = 1, ('Wrong answer')
        TL = 2, ('Time limit')
        ML = 3, ('Memory limit')
        CE = 4, ('Compilation error')
        RE = 5, ('Runtme error')
        SE = 6, ('Server error')
        NT = 7, ('Not tested')
    
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    verdict = models.IntegerField(choices=Verdicts)
    compilation_output = models.TextField()
    runtime_outputput = models.TextField()
    used_ram = models.IntegerField() #Bytes
    used_time = models.IntegerField() # Miliseconds
    solve = models.ForeignKey('Solves', on_delete=models.CASCADE)


class Solves(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.CharField(max_length=30, choices=SUPPORTED_LANGUAGES)
    code = models.TextField()



from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length= 300)
    status = models.BooleanField()
    def __str__(self) -> str:
        return f'{self.name} {self.description}'

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.name} {self.job} {self.description}'
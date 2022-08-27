from django.db import models

# Create your models here.
class Feature(models.Model):
    id: int
    name: models.CharField(max_length=100)
    description: models.CharField(max_length= 300)
    status: models.BooleanField()

class Doctor(models.Model):
    id: int
    name: models.CharField(max_length=100)
    job: models.CharField(max_length=100)
    description: models.CharField(max_length=200)
    surname: models.CharField(max_length=200)

class Pizzazz(models.Model):
    name: models.CharField()
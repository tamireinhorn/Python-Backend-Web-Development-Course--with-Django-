from django.db import models

# Create your models here.
class Feature(models.Model):
    id: int
    name: models.CharField(max_length=200)
    description: str

    def __init__(
        self, id: int, name: models.CharField(max_length=200), description: str
    ) -> None:
        self.id = id
        self.name = name
        self.description = description


class Doctor(models.Model):
    def __init__(
        self,
        id: int,
        name: models.CharField(max_length=100),
        job: models.CharField(max_length=100),
        description: models.CharField(max_length=200),
    ) -> None:
        self.id = id
        self.name = name
        self.job = job
        self.description = description

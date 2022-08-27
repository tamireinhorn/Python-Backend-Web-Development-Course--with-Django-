from django.db import models

# Create your models here.
class Feature:
    id: int
    name: str
    description: str
    def __init__(self, id: int, name: str, description: str) -> None:
        self.id = id
        self.name = name
        self.description = description


class Doctor:
    def __init__(self, id: int, name: str, job: str, description: str) -> None:
        self.id = id
        self.name = name
        self.job = job
        self.description = description
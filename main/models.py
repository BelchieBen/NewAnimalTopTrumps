from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Room(models.Model):
    code = models.CharField(max_length=4, unique = True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.host}'s room {self.code}"

class Animal(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    length = models.CharField(max_length=250)
    weight = models.CharField(max_length=250)
    lifespan = models.CharField(max_length=250)
    habitat = models.CharField(max_length=250)
    diet = models.CharField(max_length=250)
    image = models.CharField(max_length=500)


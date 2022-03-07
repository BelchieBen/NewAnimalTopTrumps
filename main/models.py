from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    code = models.CharField(max_length=4)
    host = models.ForeignKey(User, on_delete=models.CASCADE)


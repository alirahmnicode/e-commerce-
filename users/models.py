from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, unique=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

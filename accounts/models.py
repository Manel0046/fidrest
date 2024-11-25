from django.contrib.auth.models import User
from django.db import models

# Restaurante
class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()

# Cliente
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

# Recompensas
class Reward(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    points_required = models.IntegerField()

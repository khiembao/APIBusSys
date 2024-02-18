from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass




class Destination(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class SpecialOccasion(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name

class Bus(models.Model):
    model = models.CharField(max_length=50, null=False)
    bienso = models.CharField(max_length=100, null=False)
    capacity = models.IntegerField(max_length=30, null=False)

    def __str__(self):
        return self.model

class TripPath(models.Model):
    des_departed = models.ForeignKey(Destination, null=True, on_delete=True)
    des_arrived = models.ForeignKey(Destination, null=True, on_delete=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)

class Trip(models.Model):
    trip_depart_time = models.DateTimeField(null=False, blank=True)

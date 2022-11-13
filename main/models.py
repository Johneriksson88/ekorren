from django.db import models
from django.contrib.auth.models import User

SIZES = ((0, "5 m2"), (1, "6 m2"), (2, ("12 m2")))
FLOOR = ((0, 1), (1, 2))


class StorageUnit(models.Model):
    size = models.IntegerField(choices=SIZES, default=0)
    floor = models.IntegerField(choices=FLOOR, default=0)
    available = models.BooleanField(default=True)

class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.IntegerField
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

# ORDER


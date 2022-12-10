from django.db import models
from django.contrib.auth.models import User
from localflavor.se.forms import SEPersonalIdentityNumberField, SEOrganisationNumberField

StorageUnitTypeChoices = (
    ('5m2 first floor', 'S 1:st floor'),
    ('6m2 first floor', 'M 1:st floor'),
    ('10m2 first floor', 'L 1:st floor'),
    ('5m2 second floor', 'S 2:nd floor'),
    ('6m2 second floor', 'M 2:nd floor'),
    ('10m2 second floor', 'L 2:nd floor'),
    ('12m2 second floor', 'XL 2:nd floor')
    )


class StorageUnit(models.Model):
    type = models.CharField(choices=StorageUnitTypeChoices, max_length=100)
    price = models.CharField(max_length=5)

    def __str__(self):
        return self.type


class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    personnr = models.CharField(max_length=100)
    orgnr = models.CharField(max_length=100)
    company = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fullname']

    def __str__(self):
        return str(self.pk) + " " + self.fullname


class Order(models.Model):
    order_date = models.DateField(auto_now=True)
    start_date = models.DateField()
    storage_unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-order_date']

    def __str__(self):
        return 'Order ' + str(self.pk)

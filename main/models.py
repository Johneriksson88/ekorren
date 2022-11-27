from django.db import models
from django.contrib.auth.models import User

SIZES = ((0, "5 m2"), (1, "6 m2"), (2, ("12 m2")))
FLOOR = ((0, 1), (1, 2))


class StorageUnit(models.Model):
    size = models.IntegerField(choices=SIZES, default=0)
    floor = models.IntegerField(choices=FLOOR, default=0)
    available = models.BooleanField(default=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return 'Storage Unit ' + str(self.pk)


class Customer(models.Model):
    fullname = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-fullname']

    def __str__(self):
        return self.fullname


class Order(models.Model):
    order_date = models.DateField(auto_now=True)
    start_date = models.DateField()
    storage_unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-order_date']
     
    def __str__(self):
        return 'Order ' + str(self.pk)
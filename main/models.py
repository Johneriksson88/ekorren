from django.db import models
from django.contrib.auth.models import User
from localflavor.se.forms import SEPersonalIdentityNumberField, SEOrganisationNumberField

TypeChoices = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL')
    )

SizeChoices = (
    ('5 m2', '5 m2'),
    ('6 m2', '6 m2'),
    ('10 m2', '10 m2'),
    ('12 m2', '12 m2'),
)

FloorChoices = (
    ('1st', '1st'),
    ('2nd', '2nd')
)

NameChoices = (
    ('S1', 'S1'),
    ('M1', 'M1'),
    ('L1', 'L1'),
    ('S2', 'S2'),
    ('M2', 'M2'),
    ('L2', 'S2'),
    ('XL2', 'XL2')

)

class StorageUnit(models.Model):
    name = models.CharField(choices=NameChoices, max_length=100)
    type = models.CharField(choices=TypeChoices, max_length=100)
    size = models.CharField(choices=SizeChoices, max_length=100)
    floor = models.CharField(choices=FloorChoices, max_length=100)
    price = models.CharField(max_length=5)

    def __str__(self):
        return self.type


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    personnr = models.CharField(max_length=100, blank=True)
    orgnr = models.CharField(max_length=100, blank=True)
    company = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fullname']

    def __str__(self):
        return str(self.pk) + " " + self.fullname


class Order(models.Model):
    order_date = models.DateField(auto_now=True)
    start_date = models.DateField()
    storage_unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-order_date']

    def __str__(self):
        return 'Order ' + str(self.pk)

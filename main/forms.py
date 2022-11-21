from django.forms import ModelForm
from .models import StorageUnit, Customer, Order
from django.db import models


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('fullname', 'address', 'zipcode', 'city', 'email', 'phone')


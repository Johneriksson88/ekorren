from django.forms import ModelForm
from .models import StorageUnit, Customer, Order, User
from django.db import models


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('fullname', 'address', 'zipcode', 'city', 'email', 'phone')


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('storage_unit', 'start_date')


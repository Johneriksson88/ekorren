from django.forms import ModelForm
from .models import StorageUnit, Customer, Order
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('fullname', 'address', 'zipcode', 'city', 'email', 'phone')


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('storage_unit', 'start_date')


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
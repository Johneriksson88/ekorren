from django.forms import ModelForm
from .models import StorageUnit, Customer, Order
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('fullname', 'address', 'zipcode', 'city', 'email', 'phone')
        widgets = {
            'email': forms.EmailInput(),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('storage_unit', 'start_date')
        widgets = {
            'start_date': forms.widgets.SelectDateWidget()
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    
class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Your name', 'style': 'width: 80%;'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email', 'style': 'width: 80%;'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder' :'Your message here', 'style': 'width: 80%;'}))
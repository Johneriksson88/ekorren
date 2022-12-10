from django.forms import ModelForm
from .models import StorageUnit, Customer, Order, StorageUnitTypeChoices
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from collections import OrderedDict
from localflavor.se.forms import SEPersonalIdentityNumberField, SEOrganisationNumberField


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('fullname', 'address', 'zipcode', 'city', 'email', 'phone', 'personnr','company', 'orgnr' )
        widgets = {
            
            'fullname': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'John Doe'
                }),
            'address': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'King Street 1'
                }),
            'zipcode': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': '123 45'
                }),
            'city': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Stockholm'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'your@email.com'
                }),
            'phone': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': '07xxxxxxxx'
                }),
            'company': forms.CheckboxInput(),
            'personnr': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'YYYYMMDDXXXX'
                }),
            'orgnr': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'YYYYMMDDXXXX or NNNNNNNNNN'
                }),
        }

        labels = {
            'fullname': 'Full name'
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('storage_unit', 'start_date', 'customer')
        widgets = {
            'storage_unit': forms.RadioSelect(attrs={
                'style': 'max-width: 300px;'
            }),
            'start_date': forms.widgets.SelectDateWidget(attrs={
                'style': 'max-width: 300px;'
            })
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Your username'
                }),
            'password1': forms.PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                }),
            'password2': forms.PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Repeat password'
                })
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Your name', 'style': 'width: 80%;'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email', 'style': 'width: 80%;'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder' :'Your message here', 'style': 'width: 80%;'}))


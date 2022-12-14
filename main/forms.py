from django.forms import ModelForm
from .models import StorageUnit, Customer, Order, StorageUnitTypeChoices
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from collections import OrderedDict
from localflavor.se.forms import SEPersonalIdentityNumberField, SEOrganisationNumberField, SEPostalCodeField


class CustomerForm(ModelForm):
    personnr = SEPersonalIdentityNumberField()
    orgnr = SEOrganisationNumberField()
    zipcode = SEPostalCodeField()

    class Meta:
        model = Customer
        fields = ('fullname', 'address', 'zipcode', 'city', 'email', 'phone', 'personnr', 'company', 'orgnr' )
        widgets = {

            'fullname': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'John Doe'
                }),
            'address': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'King Street 1'
                }),
            'zipcode': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': '123 45'
                }),
            'city': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Stockholm'
                }),
            'email': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'your@email.com'
                }),
            'phone': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': '07xxxxxxxx'
                }),
            'company': forms.CheckboxInput(),
            'personnr': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'YYYYMMDDXXXX'
                }),
            'orgnr': forms.TextInput(attrs={
                'class': "form-control",
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
            'storage_unit': forms.RadioSelect(),
            'start_date': forms.widgets.SelectDateWidget()
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Your username'
                }),
            'password1': forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                }),
            'password2': forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Repeat password'
                })
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Your name', 'style': 'width: 80%;'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email', 'style': 'width: 80%;'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder' :'Your message here', 'style': 'width: 80%;'}))


class UpdateCustomerForm(ModelForm):
    personnr = SEPersonalIdentityNumberField()
    orgnr = SEOrganisationNumberField()
    zipcode = SEPostalCodeField()

    class Meta:
        model = Customer
        fields = ('fullname', 'address', 'zipcode', 'city', 'email', 'phone', 'personnr', 'company', 'orgnr')
        widgets = {
            
            'fullname': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'John Doe'
                }),
            'address': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'King Street 1'
                }),
            'zipcode': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': '123 45'
                }),
            'city': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Stockholm'
                }),
            'email': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'your@email.com'
                }),
            'phone': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': '07xxxxxxxx'
                }),
            'company': forms.CheckboxInput(),
            'personnr': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'YYYYMMDDXXXX'
                }),
            'orgnr': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'YYYYMMDDXXXX or NNNNNNNNNN'
                }),
        }
        labels = {
            'fullname': 'Full name'
        }

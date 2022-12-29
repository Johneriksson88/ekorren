from django.forms import ModelForm
from .models import StorageUnit, Customer, Order
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from collections import OrderedDict
from localflavor.se.forms import SEPostalCodeField


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(ModelForm):
    zipcode = SEPostalCodeField()

    class Meta:
        model = Customer
        fields = ('fullname', 'address', 'zipcode', 'city', 'email', 'phone', 'person_or_org_nr')
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
            'person_or_org_nr': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'YYYYMMDDXXXX'
                })
        }

        labels = {
            'fullname': 'Full name',
            'person_or_org_nr': 'Personnr/organisationsnr'
        }

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('storage_unit', 'start_date')
        widgets = {
            'storage_unit': forms.Select(),
            'start_date': DateInput()
        }
        labels = {
            'storage_unit': 'Pick a unit'
        }


class RegisterForm(UserCreationForm):
    username = forms.CharField(required=False)
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)

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
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'style': 'width: 80%;'
        })
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'style': 'width: 80%;'
        })
    )
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder' :'Your message here',
        'style': 'width: 80%;'
        })
    )


class UpdateCustomerForm(ModelForm):
    zipcode = SEPostalCodeField()

    class Meta:
        model = Customer
        fields = ('fullname', 'address', 'zipcode', 'city', 'email', 'phone', 'person_or_org_nr')
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
            'person_or_org_nr': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'YYYYMMDDXXXX'
                }),
        }
        labels = {
            'fullname': 'Full name',
            'person_or_org_nr': 'Personnr/orgnr'
        }

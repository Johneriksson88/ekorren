from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views import View
from .models import StorageUnit, Customer, Order
from .forms import CustomerForm, OrderForm, ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('contact_form.html', {
                'name': name,
                'email': email,
                'message': message
            })

            send_mail('subject', 'message', 'john.e.eriksson@gmail.com', ['john.e.eriksson@gmail.com'], html_message=html)
            return redirect('index')

    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})


@login_required(login_url='login')
def user_panel(request):
    return render(request, 'user_panel.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user_panel')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def customer_form(request):

    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'customer_form.html', context)


def order_form(request):

    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'order_form.html', context)


def register_form(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = UserCreationForm()

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account successfully created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'register_form.html', context)
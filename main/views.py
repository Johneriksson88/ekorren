from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views import View
from django.views.generic import CreateView
from .models import StorageUnit, Customer, Order
from .forms import CustomerForm, OrderForm, RegisterForm, ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy


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


def order_success(request):
    return render(request, 'order_success.html')

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
    """ if request.user.is_authenticated:
        return redirect('index')
    else:
         """
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


def multi_form(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)
        register_form = RegisterForm(request.POST)

        if customer_form.is_valid() and order_form.is_valid() and register_form.is_valid():
            customer = customer_form.save()
            order = order_form.save(False)
            user = register_form.save(False)
            
            customer.order = customer
            order.save()
            customer.user = customer
            user.save()

            return redirect(reverse_lazy('order_success'))
    else:
        customer_form = CustomerForm()
        order_form = OrderForm()
        register_form = RegisterForm()

    args = {}
    args.update(csrf(request))
    args['customer_form'] = customer_form
    args['order_form'] = order_form
    args['register_form'] = register_form

    return render(request, "multi_form.html", args)
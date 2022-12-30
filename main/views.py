from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import StorageUnit, Customer, Order
from .forms import CustomerForm, OrderForm, RegisterForm, ContactForm, UpdateCustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from datetime import datetime
import csv
from django.contrib.admin.views.decorators import staff_member_required


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
            messages.success(request, 'Thank you for contacting us! We will get back to you shortly.')
            return redirect('index')

    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})


# HOW DO I CHECK IF THE USER HAS A CUSTOMER ATTATCHED AND IF NOT CREATE A NEW CUSTOMER CONNECTED TO THE USER?
# BELOW IF STATEMENT DOESNT WORK
@login_required(login_url='login')
def user_panel(request):

    """ customers = Customer.objects.all()
    customers = customers.filter(user=request.user)
    if customers:
        customer = Customer.objects.get(user=request.user)
        print("User has customer")
    else:
        new_customer = Customer.objects.create(user=request.user)
        new_customer.save()
        print("New customer created")
        return redirect('customer_form')
 """
    customer = Customer.objects.get(user=request.user)
    if customer.fullname.__len__() < 1:
        return redirect('customer_form')
    
    # Hide last 4 digits of person number

    """ personnr = request.user.customer.personnr
    size = len(request.user.customer.personnr)
    replacement = "****"
    personnr = personnr.replace(personnr[size - 4:], replacement) """

    orders = request.user.customer.order_set.all()

    if request.method == 'POST':
        update_customer_form = UpdateCustomerForm(request.POST, instance=request.user.customer)
        if update_customer_form.is_valid():
            update_customer_form.save()
            messages.success(request, 'Your information has been updated.')
            return redirect('user_panel')

    else:
        update_customer_form = UpdateCustomerForm(instance=request.user.customer)

    context = {'orders': orders, 'update_customer_form': update_customer_form, 'customer': customer}
    return render(request, 'user_panel.html', context)


def order_success(request):
    return render(request, 'order_success.html')


def register_success(request):
    return render(request, 'register_success.html')


def user_login(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('user_panel')
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
    messages.info(request, 'You have been logged out.')
    return redirect('index')


def customer_form(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Your information was successfully added!")
            return redirect('user_panel')
        else:
            form = CustomerForm()

    context = {'form': form}
    return render(request, 'customer_form.html', context)

@login_required(login_url='login')
def order_form(request):
    units = StorageUnit.objects.all().values_list('name', 'size', 'price')
    customer = Customer.objects.get(user=request.user)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.customer = customer
            form.save()
            messages.success(request, "Order successfully submitted! You will get an email confirmation shortly.")
            return redirect("user_panel")

    context = {'form': form, 'units': units}
    return render(request, 'order_form.html', context)


def register_form(request):

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            """ form.save() """
            user = form.save()
            Customer.objects.create(
                user=user
            )
            username = form.cleaned_data.get('username')
            print(user.customer)
            messages.success(request, 'Account successfully created for ' + username)
            return redirect('user_panel')

    context = {'form': form}
    return render(request, 'register_form.html', context)

"""
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
            messages.success(request, "Thank you for your order! You will recieve an email confimation shortly.")
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

 """

"""
def multi_form(request):
    
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)

        if customer_form.is_valid() and order_form.is_valid():
            customer = customer_form.save()
            order = order_form.save(commit=False)
            print(customer)
            order.save()
            
            messages.success(request, "Thank you for your order! You will recieve an email confimation shortly.")
            return redirect(reverse_lazy('index'))
    else:
        customer_form = CustomerForm()
        order_form = OrderForm()

    args = {}
    args.update(csrf(request))
    args['customer_form'] = customer_form
    args['order_form'] = order_form

    return render(request, "multi_form.html", args) 
    """


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


def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('user_panel')
    context = {'order': order}
    return render(request, 'delete_order.html', context)


def delete_account(request, pk):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.delete()
        logout(request)
        messages.info(request, 'Your account has been successfully deleted.')
        return redirect('index')
    context = {'user': user}
    return render(request, 'delete_account.html', context)


@staff_member_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Namn', 'Adress', 'Postnummer', 'Stad', 'Email', 'Telefon', 'Personnr', 'Organisationsnr'])
    for customer in Customer.objects.all().values_list('fullname', 'address', 'zipcode', 'city', 'email', 'phone', 'personnr', 'orgnr'):
        writer.writerow(customer)

    response['Content-Disposition'] = 'attatchment; filename="customers.csv"'
    return response
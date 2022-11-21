from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from .models import StorageUnit, Customer, Order
from .forms import CustomerForm


def index(request):
    return render(request, 'index.html')


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")


def user_panel(request):
    return render(request, 'user_panel.html')


def user_login(request):
    return render(request, 'user_login.html')

def customer_form(request):

    form = CustomerForm()
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'form.html', context)
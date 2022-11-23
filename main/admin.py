from django.contrib import admin
from .models import StorageUnit, Customer, Order


my_models = [StorageUnit, Customer, Order]
admin.site.register(my_models)
from django.urls import path
from . import views
from main.views import customer_form, register_form, order_form

urlpatterns = [
    path("", views.index, name='index'),
    path("customerform/", views.customer_form, name='customer_form'),
    path("orderform/", views.order_form, name='order_form'),
    path("login/", views.user_login, name='login'),
    path("logout/", views.user_logout, name='logout'),
    path("user_panel/", views.user_panel, name='user_panel'),
    path("register/", views.register_form, name='register'),
]
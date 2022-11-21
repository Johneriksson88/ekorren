from django.urls import path
from . import views
from main.views import customer_form

urlpatterns = [
    path("", views.index, name='index'),
    path("sections/<int:num>", views.section, name='section'),
    path("form/1", views.customer_form),
    path("form/2", views.order_form),
    path("form/3", views.user_form),
    path("login/", views.user_login),
    path("user_panel/", views.user_panel),
    path("register/", views.user_form),
]
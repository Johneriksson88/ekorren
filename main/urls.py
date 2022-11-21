from django.urls import path
from . import views
from main.views import customer_form

urlpatterns = [
    path("", views.index, name='index'),
    path("sections/<int:num>", views.section, name='section'),
    path("form/", views.customer_form)
]
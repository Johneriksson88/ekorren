from django.urls import path
from . import views
from main.views import user_panel, user_login

urlpatterns = [
    path("", views.index, name='index'),
    path("sections/<int:num>", views.section, name='section'),
    path("user_panel/", user_panel),
    path("user_login/", user_login),
]
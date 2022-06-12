from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("ad/", views.admin, name="admin"),
    path("man/", views.man, name="man"),
    path("dev/", views.dev, name="dev"),
]

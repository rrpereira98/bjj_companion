from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_tournment/", views.create_tournment, name="create tournment")
]

from django.urls import path

from . import views

urlpatterns = [
    path("shorten/", views.shorten),
]

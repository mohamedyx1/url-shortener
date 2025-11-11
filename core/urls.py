from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shorten/", views.shorten, name="shorten"),
    path("detail/<slug:code>/", views.detail, name="detail"),
    path("delete/<slug:code>/", views.delete, name="delete"),
    path("<slug:code>/", views.redirect_entry, name="redirect_entry"),
]

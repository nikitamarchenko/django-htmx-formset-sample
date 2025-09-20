from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-form", views.add_form, name="index-add-form"),
]

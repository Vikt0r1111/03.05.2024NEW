from django.contrib import admin
from django.urls import path
from .views import contact_form

urlpatterns = [
    path('', contact_form, name="contact_form"),
]


from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('Simple ERP/',views.personform),
    path('cc/',views.c, name='cpage')

]

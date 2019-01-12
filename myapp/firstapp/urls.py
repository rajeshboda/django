from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('countries/', views.countries),
    path("countryinfo/", views.country_info),

]

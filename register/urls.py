
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('list/', views.list, name='list'),
    path('search/', views.search, name='search'),

]
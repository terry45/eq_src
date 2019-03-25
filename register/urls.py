from django.contrib import admin
from django.urls import path
from . import views
from .views import DeviceListView

urlpatterns = [
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('', DeviceListView.as_view(), name='list')
]

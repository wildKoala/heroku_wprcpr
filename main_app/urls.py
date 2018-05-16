from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_material', views.add_material),
    ]

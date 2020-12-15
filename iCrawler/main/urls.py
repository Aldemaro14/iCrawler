from django.urls import path, include
#from django.http import request
from . import views

urlpatterns = [
    path('product/', views.getProduct , name='product'),
    path('variations/', views.getVariations, name='variations'),
]

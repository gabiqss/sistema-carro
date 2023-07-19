from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_carro, name='forms-carros'),
]
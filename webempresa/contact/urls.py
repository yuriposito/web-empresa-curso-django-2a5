from django.urls import path
from . import views

urlpatterns = [
     #Paths del nucleo
    path('', views.contact, name='contact'),

]

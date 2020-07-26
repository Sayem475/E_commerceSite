from django.urls import path, include
from . import views
from django.views import View
from .views import Home, Registration, Login, Checkout, Contact, About, Search

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('registration',Registration.as_view(), name='registration'),
    path('contact',Contact.as_view(), name='contact'),
    path('login',Login.as_view(), name='login'),
    path('search',Search.as_view(), name='search'),
    path('checkout',Checkout.as_view(), name='checkout'),
]
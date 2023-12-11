from django.urls import path
from .views import about, redirect_urls,home

urlpatterns= [
    path('',home, name='index'),
    path('<slug>/',redirect_urls, name='redirect_urls'),
    path('about-me',about, name='about'),

]
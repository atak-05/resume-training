from django.urls import path
from .views import about, redirect_urls

urlpatterns= [
    path('',about, name='index'),
    path('<slug>/',redirect_urls, name='redirect_urls'),
    path('about-me',about, name='about'),

]
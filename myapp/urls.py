from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('submit/', views.submit, name='submit'),
    path('users/', views.users, name='users'),
    path('contact/', views.contact, name='contact'),
]

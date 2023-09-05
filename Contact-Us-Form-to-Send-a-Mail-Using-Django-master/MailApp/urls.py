from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactform, name='contactform'),
    path('contact', views.contact, name='contact'),

]

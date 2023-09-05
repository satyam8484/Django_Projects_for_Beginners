from django.urls import path
from . import views

urlpatterns = [
    path('', views.verify, name='verify'),
    path('email_verification_code', views.email_verification_code, name='email_verification_code'),
    path('send_Gmail',views.send_Gmail,name='send_Gmail')
]

from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Insert_view),
    path('show',views.show),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update),
    path("logout",views.logout,name="logout")
]
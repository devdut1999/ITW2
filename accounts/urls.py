
from django.urls import path, include
from . import views

urlpatterns = [
   path('login', views.loginPage, name='login'),
    path('signup', views.register, name='signup'),
    path('logout', views.logoutUser, name='logout'),
   
]
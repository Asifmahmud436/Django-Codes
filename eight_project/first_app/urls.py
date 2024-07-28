from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('/signup',views.Signup,name='signup'),
    path('/profile',views.profile,name='profile'),
    path('/login',views.user_login,name='login'),
    path('/logout',views.user_logout,name='logout'),
    path('/passchange',views.pass_change,name='passchange'),
    path('/passchange2',views.pass_change2,name='passchange2'),
    path('',views.home,name='home')
]
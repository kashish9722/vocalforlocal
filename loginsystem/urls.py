from django.contrib import admin
from django.urls import path
from loginsystem import views


urlpatterns = [

    path("login" , views.login , name='login'),
    
    path("loginc" , views.loginc , name='loginc'),

    path("registerc" , views.registerc , name='registers'),

    path("registers" , views.registers, name='registerc'),

]
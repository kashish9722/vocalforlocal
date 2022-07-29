from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "vocal-for-local Admin"
admin.site.site_title = "vocal-for-local Admin Portal"
admin.site.index_title = "Welcome to vocal-for-local"

urlpatterns = [

    path("" , views.home , name='home'),
    path("home" , views.home , name='home'),
    path("about" , views.about , name='about'),
    path("Account" , views.account , name='account'),
  
    
      
  
]
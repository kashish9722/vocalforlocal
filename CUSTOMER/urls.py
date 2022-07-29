from django.contrib import admin
from django.urls import path
from CUSTOMER import views


urlpatterns = [
      path("list" , views.list , name='list')
]
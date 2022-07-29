from django.contrib import admin
from django.urls import path
from SELLER import views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("Account/login/profile" , views.profile , name='profile'),
    path("Account/login/addproduct" , views.addproduct , name='addproduct'),
    
    #path("Account/login/forms" , views.addproduct , name='addproduct'),

]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
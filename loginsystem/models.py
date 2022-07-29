from django.db import models

# Create your models here.
class Sample1 (models.Model):
    id = models.AutoField(primary_key=True) 
    flname = models.CharField(max_length=30) 
    pnumber= models.CharField(max_length=10)
    email = models.EmailField(max_length=50) 
    password = models.CharField(max_length=32) 
    repassword = models.CharField(max_length=32) 
class pSELLER (models.Model):
    id = models.AutoField(primary_key=True) 
    flname = models.CharField(max_length=30) 
    username = models.CharField(max_length=30) 
    zip = models.CharField(max_length=32) 
    state = models.CharField(max_length=32) 
    city = models.CharField(max_length=32) 
    email = models.EmailField(max_length=50) 
    pnumber= models.CharField(max_length=10)
    password = models.CharField(max_length=32) 
    repassword = models.CharField(max_length=32)
    address = models.CharField(max_length=100) 
    iurl = models.URLField(max_length=150) 
    desc = models.CharField(max_length=500) 
    def __str__(self):
         return self.flname
   
    
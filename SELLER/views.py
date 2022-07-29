from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,redirect 
from django.contrib import messages
from .forms import productform
from .models import product
from django.db import connections
import mysql.connector
from operator import itemgetter
from loginsystem.models import pSELLER
from loginsystem.forms import pSELLERform

# Create your views here.
def profile(request):
   
     return render(request, 'forms.html')
def addproduct(request):
     if request.method =="POST":
           print('THIS IS POST')
          
           products= product()
          
           products.pname=request.POST.get('pname')
           
           products.category = request.POST.get('category')
           products.img = request.POST.get('img')
           products.iurl = request.POST.get('iurl')
           products.desc = request.POST.get('desc')
            
           if products.pname=="" or  products.category=="" or products.img =="" :

                messages.info(request,"Some fields are missing")
                return redirect('addproduct')   
           else:
                #  con = mysql.connector.connect(host="localhost",user="root",
                #  passwd="kashish@48",database="loginsystem")
                #  cursor = con.cursor()
                #  sqlcommand = "select username from loginsystem_pSELLER"
                #   result123[]
                #  rows[]
                #  result123=cursor.execute(sqlcommand)
                #  rows = result123.fetchall()
                #  for result123 in rows:
                #  #if request.method =="POST":
                #    #username = request.POST['username']
                  
                #    if result123==username :

                #      products.save
                #      return redirect('profile')
                      
                #  else:
                #        return redirect('addproduct')
                 con = mysql.connector.connect(host="localhost",user="root",
                 passwd="kashish@48",database="loginsystem")
                 cursor = con.cursor()
                
                 sqlcommand = "select username from loginsystem_pSELLER"
        
                 cursor.execute(sqlcommand)
        
                 u=[]
       
       
                 for i in cursor:
                     u.append(i)
        
                 res = list(map(itemgetter(0), u))
        
                 if request.method =="POST":
                     username = request.POST.get('username')
                     #password = request.POST['password']
                     k=len(res)
                     i=0
            
            
                     while i <k:
                        
                
           
                        if res[i]==username :
                           products.save()  
                           return render(request,'profile.html')
                           break
                        i+=1
                     else:
                           return redirect('login')


     return render(request,'addproduct.html')   
               

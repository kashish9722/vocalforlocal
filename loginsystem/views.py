from django.shortcuts import render,redirect 
from django.contrib import messages
from .forms import Sample1form,pSELLERform
from .models import Sample1, pSELLER
from django.db import connections
import mysql.connector
from operator import itemgetter

    
def login(request):
        con = mysql.connector.connect(host="localhost",user="root",
        passwd="kashish@48",database="loginsystem")
        cursor = con.cursor()
        con2 = mysql.connector.connect(host="localhost",user="root",
        passwd="kashish@48",database="loginsystem")
        cursor2 = con2.cursor()
        sqlcommand = "select email from loginsystem_pSELLER"
        sqlcommand2 = "select password from loginsystem_pSELLER"
        cursor.execute(sqlcommand)
        cursor2.execute(sqlcommand2)
        e=[]
        p=[]
       
        for i in cursor:
            e.append(i)
        for j in cursor2:
            p.append(j)
        res = list(map(itemgetter(0), e))
        res2 = list(map(itemgetter(0), p))    
        con3 = mysql.connector.connect(host="localhost",user="root",
        passwd="kashish@48",database="loginsystem")
        cursor3 = con2.cursor()

        if request.method =="POST":
            email = request.POST['email']
            password = request.POST['password']
            k=len(res)
            i=1
            sqlcommand3 = "select flname from loginsystem_pSELLER where email = email"
            cursor3.execute(sqlcommand3)
            lst =[]
            for name in cursor3:
                name = name
                name2 =''.join(name)
                i=0;
            print(name2)
            while i <k:
                
           
               if res[i]==email and res2[i]==password:
                   return render(request,'profile.html',{'name':name2})
                   messages.success(request, "Successfully Logged In")
                    #return redirect('profile')
                   break
               i+=1
            else:
             
                messages.error(request,"Check email or password")
                return redirect('login')

        return render(request,'login.html')   
        return render(request,'welcome.html')
     
def loginc(request):
        con = mysql.connector.connect(host="localhost",user="root",
        passwd="kashish@48",database="loginsystem")
        cursor = con.cursor()
        con2 = mysql.connector.connect(host="localhost",user="root",
        passwd="kashish@48",database="loginsystem")
        cursor2 = con2.cursor()
        sqlcommand = "select email from loginsystem_Sample1"
        sqlcommand2 = "select password from loginsystem_Sample1"
        cursor.execute(sqlcommand)
        cursor2.execute(sqlcommand2)
        e=[]
        p=[]
       
        for i in cursor:
            e.append(i)
        for j in cursor2:
            p.append(j)
        res = list(map(itemgetter(0), e))
        res2 = list(map(itemgetter(0), p))    
        con3 = mysql.connector.connect(host="localhost",user="root",
        passwd="kashish@48",database="loginsystem")
        cursor3 = con2.cursor()

        if request.method =="POST":
            email = request.POST['email']
            password = request.POST['password']
            k=len(res)
            i=1
            sqlcommand3 = "select flname from loginsystem_Sample1 where email = email"
            cursor3.execute(sqlcommand3)
            lst =[]
            for name in cursor3:
                name = name
                name2 =''.join(name)
                i=0;
            print(name2)
            while i <k:
                
           
               if res[i]==email and res2[i]==password:
                   messages.success(request, "Successfully Logged In")
                   return render(request,'choose.html',{'name':name2})
                    #return redirect('profile')
                   break
               i+=1
            else:
             
                messages.error(request,"Check email or password")
                return redirect('loginc')

        return render(request,'loginc.html')   
        return render(request,'welcome.html')
     

     

def registers(request):
     if request.method =="POST":
           print('THIS IS POST')
           #seller = Newregisterc(request.POST, request.FILES)
           seller= pSELLER ()
          
           seller.flname=request.POST['flname']
           seller.username=request.POST['username']
           seller.pnumber = request.POST['pnumber']
           seller.email = request.POST['email']
           seller.password = request.POST['password']
           seller.repassword = request.POST['repassword']
           seller.city = request.POST['city']
           seller.state = request.POST['state']
           seller.address = request.POST['zip']
           seller.iurl = request.POST['zip']
           seller.desc = request.POST['zip']
           seller.zip = request.POST['zip']
           if seller.password!=seller.repassword:
                messages.error(request,"Passwords not match")
                return redirect('registers')  
           elif seller.flname=="" or  seller.email=="" or seller.password =="" or seller.repassword=="":

                messages.error(request,"Some fields are missing")
                return redirect('registers')   
           else:
                messages.success(request,"registration is done ")
                #HttpResponse("done")
                seller.save()
                #return redirect ('login')
            
           
           #return render(request,'registers.html')
     return render(request, 'registers.html')
def registerc(request):
        
      if request.method =="POST":
           print('THIS IS POST')
           #seller = Newregisterc(request.POST, request.FILES)
          
           sample1= Sample1 ()
           sample1.email = request.POST['email']
           sample1.flname=request.POST['flname']
           sample1.pnumber = request.POST['pnumber']
           sample1.password = request.POST['password']
           sample1.repassword = request.POST['repassword']
           if sample1.password!=sample1.repassword:
                messages.error(request,"Passwords not match")
                return redirect('registerc')  
           elif sample1.flname=="" or  sample1.email=="" or sample1.password =="" or sample1.repassword=="":

                messages.error(request,"Some fields are missing")
                return redirect('registerc')   
           else:
                messages.error(request,"registration is done ")
                #HttpResponse("done")
                sample1.save()
                return redirect ('loginc')
            
      return render(request,'registerc.html')   
           

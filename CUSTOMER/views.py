from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,redirect 
from django.contrib import messages
from SELLER.forms import productform
from SELLER.models import product
from django.db import connections
import mysql.connector
from operator import itemgetter
from loginsystem.models import pSELLER
from loginsystem.forms import pSELLERform
from math import ceil


# Create your views here.
def list(request):
    products= product.objects.all()
    allProds=[]
    catprods= product.objects.values('category')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"display.html", params  )     
           #return render(request,"choose.html")
from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return render(request, 'home.html')
   
def about(request):
     return render(request, 'about.html')

def home(request):
     return render(request, 'home.html')
def account (request):
     return render(request, 'welcome.html')

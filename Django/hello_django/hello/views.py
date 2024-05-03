from django.shortcuts import render
from django.http import *
from django.forms import *


# Create your views here.
def home(request):
    return HttpResponse('<h1>"Hello, World"</h1>')

def wellcome(request):
    return render(request,"index.html")

def sayhello(request):
    user = request.POST.get("user")
    return render(request,"sayhello.html",{"name":user})
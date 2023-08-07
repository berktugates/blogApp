from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"blog/home.html")

def discover(request):
    return render(request, "blog/discover.html")

def account(request):
    return render(request, "blog/account.html")

def aboutus(request):
    return render(request, "blog/aboutus.html")
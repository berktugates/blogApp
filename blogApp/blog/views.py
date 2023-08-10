from django.shortcuts import render
from blog.models import Blog,Category

# Create your views here.

def home(request):
    context = {
        "blogs" : Blog.objects.all(),
        "category" : Category.objects.all()
    }
    return render(request, "blog/home.html", context)

def discover(request):
    context = {
        "blogs" : Blog.objects.all()
    }
    return render(request, "blog/discover.html",context)

def account(request):
    return render(request, "blog/account.html")

def aboutus(request):
    return render(request, "blog/aboutus.html")
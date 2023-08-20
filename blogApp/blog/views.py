from django.shortcuts import render
from blog.models import Blog,Category,TopWeek,Softwarelang

# Create your views here.

def home(request):
    context = {
        "blogs" : Blog.objects.all(),
        "category" : Category.objects.all(),
        "topweek" : TopWeek.objects.all()
    }
    return render(request, "blog/home.html", context)

def discover(request):
    context = {
        "languages" : Softwarelang.objects.all(),
        "topweek" : TopWeek.objects.all()
    }
    return render(request, "blog/discover.html",context)

def discover_blog_details(request,slug):
    selectedBlog = None
    languages = Softwarelang.objects.all()
    for l in languages:
        if l.slug == slug:
            selectedBlog = l

    context={
        "blog" : selectedBlog,
        "category" : Category.objects.all(),
        "topweek" : TopWeek.objects.all()

    }
    return render(request,"blog/discovery_blog_details.html",context)

def blogs_by_category(request, slug):
    context={
        "blogs": Blog.objects.filter(is_active=True, categories__slug=slug),
        "category" : Category.objects.all(),
        "selected_category" : slug
    }
    return render(request, "blog/blogs_by_category.html", context)

def blog_details(request, slug):
    selectedBlog = None
    blogs = Blog.objects.filter(is_active=True) 
    for blog in blogs:
        if blog.slug == slug:
            selectedBlog = blog
    context={
        "blog" : selectedBlog,
        "category" : Category.objects.all(),
        "topweek" : TopWeek.objects.all()
    }          
    return render(request, "blog/blog_details.html",context)
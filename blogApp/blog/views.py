from django.shortcuts import render
from blog.models import Blog,Category,TopWeek

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
        "blogs" : Blog.objects.all(),
        "topweek" : TopWeek.objects.all()
    }
    return render(request, "blog/discover.html",context)

def blogs_by_category(request, slug):
    context={
        "blogs": Blog.objects.filter(is_active=True, categories__slug=slug),
        "category" : Category.objects.all(),
        "selected_category" : slug
    }
    return render(request, "blog/blogs_by_category.html", context)

def blog_details(request, id):
    selectedBlog = None
    blogs = Blog.objects.filter(is_active=True) 
    for blog in blogs:
        if blog.id == id:
            selectedBlog = blog
    context={
        "blog" : selectedBlog,
        "category" : Category.objects.all(),
        "topweek" : TopWeek.objects.all()
    }          
    return render(request, "blog/blog_details.html",context)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name= "home"),
    path("discover/", views.discover, name = "discover"),
    path("discover/<slug:slug>",views.discover_blog_details, name="discovery_blog_details"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blog/<slug:slug>", views.blog_details, name="blog_details")
]

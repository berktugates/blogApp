from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name= "home"),
    path("discover/", views.discover, name = "discover"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blog/<int:id>", views.blog_details, name="blog_details")
]

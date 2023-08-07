from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name= "home"),
    path("discover/", views.discover, name = "discover"),
    path("account/", views.account, name = "account"),
    path("aboutus/", views.aboutus, name = "aboutus")
]

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"account/login.html",{
                "error" : "Kullanıcı adı veya parola yanlış."
            })    
    return render(request, "account/login.html")

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(request, "account/register.html", {
                    "error" : "Bu kullanıcı adına sahip bir kullanıcı bulunmaktadır."
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {
                        "error" : "Bu mail kullanılmaktadır."
                    })
                else:
                    user = User.objects.create_user(username=username, first_name=name, last_name=surname, email=email)
                    user.save()
                    return redirect("login")
        else:
            return render(request, "account/register.html",{
                "error" : "Şifreler birbiriyle uyuşmuyor."
            })
    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")
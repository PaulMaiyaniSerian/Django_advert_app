from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from homepage.views import homepage
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def register_user(request):
    if request.method == "GET":
        form = RegisterForm()
        context = {
            'form' : form,
        }
        return render(request, "register.html", context)
    else:
       form = RegisterForm(request.POST)
       context = {
           'form' : form,
       }
       if form.is_valid():
           form.save()
           return redirect(login_user)
       else:
           return render(request, "register.html", context)
        
    #    return render(request, "register.html", context) 

def login_user(request):
    if request.method == "GET":
        
        return render(request, "login.html")

    else:
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(homepage)
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect(login_user)
    
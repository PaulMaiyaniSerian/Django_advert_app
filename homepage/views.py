from django.shortcuts import render, redirect
from .models import Contact, Subscribe
# Create your views here.
def homepage(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        call_time = request.POST['call_time']
        comments = request.POST['comments']

        message = Contact.objects.create(name=name, email=email, phone=phone,time=call_time, comments=comments)
      
        return redirect(homepage)

def contacts(request):
    if request.method == "GET":
        return render(request, 'contactus.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        call_time = request.POST['call_time']
        comments = request.POST['comments']

        message = Contact.objects.create(name=name, email=email, phone=phone,time=call_time, comments=comments)

        return redirect(contacts, permanent=True)

def about_us(request):
    if request.method == "GET":
        return render(request, "about.html")
    else:
        sub = request.POST['email']
        if Subscribe.objects.filter(email=sub).exists():
            return redirect(about_us)

        subscriber = Subscribe.objects.create(email=sub, subscribe_status=1)
    
        return redirect(about_us)
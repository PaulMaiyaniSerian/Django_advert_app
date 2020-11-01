from django.shortcuts import render
from .models import Tutorial
# Create your views here.
def tutorial(request):
    if request.method == "GET":
        tutorials = Tutorial.objects.all()
        context = {
            "tutorials":tutorials,
        }
        return render(request,"tutorial.html", context)
from django.shortcuts import render, redirect
from .models import Gallery, OtherGallery
# Create your views here.
def gallery_view(request):
    if request.method == "GET":
        items = Gallery.objects.all()
        otheritems = OtherGallery.objects.all()

        context = {
            "items": items,
            "other_items": otheritems,
        }

        return render(request, 'Gallery.html', context)
    else:
        return render(request, 'Gallery.html', context)
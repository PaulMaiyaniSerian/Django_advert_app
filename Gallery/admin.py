from django.contrib import admin

# Register your models here.
from .models import Gallery,OtherGallery

admin.site.register(Gallery)
admin.site.register(OtherGallery)



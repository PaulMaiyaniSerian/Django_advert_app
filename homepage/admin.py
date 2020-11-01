from django.contrib import admin

# Register your models here.
from .models import Contact, Subscribe
admin.site.register(Contact)
admin.site.register(Subscribe)
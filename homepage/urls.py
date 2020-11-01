from django.urls import path
from .views import homepage, contacts, about_us
urlpatterns = [
    path('',homepage, name="homepage"),
    path('contacts/',contacts, name="contacts"),
    path('about_us/',about_us, name="about_us"),
    
]

from django.urls import path
from .views import tutorial

urlpatterns = [
    path('tutorials', tutorial, name="tutorial"),
]

from django.urls import path
from .views import gallery_view

urlpatterns = [
    path('view_gallery/', gallery_view, name="view_gallery_items"),
]

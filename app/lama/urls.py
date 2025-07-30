"""URLs for lama."""
from django.urls import path
from .views import InpaintView

app_name = 'lama'


urlpatterns = [
    path('inpaint/', InpaintView.as_view(), name='inpaint'),
]
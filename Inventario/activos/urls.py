# activos/urls.py

from django.urls import path
from .views import escanear_archivo

urlpatterns = [
    path('escanear_archivo/', escanear_archivo, name='escanear_archivo'),
]

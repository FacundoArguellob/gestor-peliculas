from django.urls import path
from . import views

urlpatterns = [
    path('', views.prueba_template, name='inicio'),
]

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'peliculas/index.html')

def login(request):
    return render(request, 'peliculas/login.html')

def register(request):
    return render(request, 'peliculas/register.html')

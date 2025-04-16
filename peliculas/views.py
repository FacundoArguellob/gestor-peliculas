from django.shortcuts import render

# Create your views here.


def prueba_template(request):
    return render(request, 'peliculas/index.html')

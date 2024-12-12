from django.shortcuts import render
from .models import Producto

def landing(request):
    productos = Producto.objects.all()
    return render(request, 'inicio.html', {'productos': productos})

def productos(request):
    productos = Producto.objects.all()  
    return render(request, 'productos.html', {'productos': productos})


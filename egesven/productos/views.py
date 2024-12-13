from django.shortcuts import render,redirect
from .models import Producto
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def landing(request):
    productos = Producto.objects.all()
    return render(request, 'inicio.html', {'productos': productos})

def productos(request):
    productos = Producto.objects.all()  
    return render(request, 'productos.html', {'productos': productos})


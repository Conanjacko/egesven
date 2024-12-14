from django.shortcuts import render
from util.auth import session_required

from .models import Producto


@session_required
def landing(request):
    productos = Producto.objects.all()

    return render(request, "inicio.html", {"productos": productos})


def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {"productos": productos})

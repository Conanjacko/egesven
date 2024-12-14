import json
import urllib.parse

from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.shortcuts import render

from .models import Producto


def landing(request):
    productos = Producto.objects.all()

    return render(request, "inicio.html", {"productos": productos})


def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {"productos": productos})


def carrito(request):
    sessionid = request.COOKIES.get("sessionid")
    is_authenticated = False
    user = None
    if sessionid:
        try:
            session = Session.objects.get(session_key=sessionid)
            user_id = session.get_decoded().get("_auth_user_id")

            if user_id:
                User = get_user_model()
                user = User.objects.get(id=user_id)

                if user:
                    is_authenticated = True
        except Session.DoesNotExist:
            pass

    cart_param = request.GET.get("cart")
    cart = {}
    if cart_param:
        decoded_cart = urllib.parse.unquote(cart_param)
        try:
            cart = json.loads(decoded_cart)
        except json.JSONDecodeError:
            pass

    productos_en_carrito = []
    total = 0

    for p, id in cart.items():
        try:
            producto = Producto.objects.get(id=id)
            total_producto = producto.precio
            productos_en_carrito.append(
                {
                    "producto": producto,
                    "cantidad": 1,
                    "total_producto": f"${producto.precio:,.0f}",
                }
            )
            total += total_producto
        except Producto.DoesNotExist:
            continue
    total_formateado = f"${total:,.0f}"
    return render(
        request,
        "carrito.html",
        {
            "productos": productos_en_carrito,
            "total": total_formateado,
            "is_authenticated": is_authenticated,
            "user": user,
        },
    )

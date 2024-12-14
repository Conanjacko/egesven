from django.urls import path

from .views import carrito, landing, productos

app_name = "productos"

urlpatterns = [
    path("", productos, name="home"),
    path("landing/", landing, name="landing"),
    path("carrito/", carrito, name="carrito"),
]

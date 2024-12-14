from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import RegistroForm


def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            return redirect("usuarios:login")  # Ajusta según tu URL de inicio de sesión
    else:
        form = RegistroForm()
    return render(request, "users/registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)

            return redirect(reverse("inicio"))
        else:
            return HttpResponse("Usuario o contraseña incorrectos.")
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)

    return redirect(reverse("inicio"))

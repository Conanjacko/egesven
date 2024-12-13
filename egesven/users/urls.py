from django.urls import path
from . import views
from .views import login_view, registro_view, logout_view

app_name = 'usuarios'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registro/', registro_view, name='registro'),
    path('logout/', logout_view, name='logout'),
]
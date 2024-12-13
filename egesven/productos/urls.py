from django.urls import path
from .views import landing, productos 

app_name = 'productos'

urlpatterns = [
    path('', productos, name='home'),
    path('landing/', landing, name='landing'),  
]
from django.shortcuts import render
from .models import Producto

# Create your views here.
def home(request):
    return render(request, 'home.html', context={})

def crear_producto(request, nombre):
    producto = Producto.objects.create(name = nombre ,price=350, fecha="2022-8-23")
    context = { 'producto': producto, }
    return render(request, "home.html", context)

def ver_producto(request):
    productos = Producto.objects.all()
    context = { 'productos': productos, }
    return render(request, "home.html", context)
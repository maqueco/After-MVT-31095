from django.urls import path
from Producto.views import ver_producto, crear_producto

urlpatterns = [
    path('product/', ver_producto, name ="product"),
    path('crear/<nombre>', crear_producto)
]

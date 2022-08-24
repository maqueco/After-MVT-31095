from django.contrib import admin
from django.urls import path
from Producto.views import ver_producto, crear_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',home)
    path('product/', ver_producto),
    path('crear/<nombre>', crear_producto)
]

from django.urls import path
from .views import lista_inventario, per_product_view, anadir_producto, borrar_producto, actualizar_producto, exportar # Import de los url en el index.html

urlpatterns = [
    path("", lista_inventario, name="lista_inventario"),
    path("per_product/<int:pk>", per_product_view, name="vista_producto"),
    path("anadir_inventario", anadir_producto, name="anadir_formulario"),
    path("borrar_producto<int:pk>", borrar_producto, name="borrar_producto"),
    path("actualizar_producto<int:pk>", actualizar_producto, name="actualizar_producto"),
    path("exportar_csv", exportar, name="exportar")
]
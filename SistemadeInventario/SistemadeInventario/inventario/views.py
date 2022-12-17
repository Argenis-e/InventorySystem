from django.shortcuts import get_object_or_404, render, redirect
from .models import Inventario
from django.contrib.auth.decorators import login_required
from .forms import Anadir, Actualizar
from django.http import HttpResponse

import csv # Para hacer exports

# Create your views here.

@login_required
def lista_inventario(request):
    inventories = Inventario.objects.all() # Agrega los objetos en la clase Inventario
    context = { # Los diferentes títulos que se pueden heredar
        "title": "Lista de inventario",
        "inventories": inventories
    }
    return render(request, "inventario/lista_inventario.html", context=context)

@login_required
def per_product_view(request, pk): # vista de un producto específico pk= Primary Key
    inventario = get_object_or_404(Inventario, pk=pk)
    context = {
        'inventario': inventario
    }

    return render(request, "inventario/per_product.html", context=context)

@login_required
def anadir_producto(request): # Formulario para añadir objetos
    if request.method == "POST":
        anadir_formulario = Anadir(data=request.POST)
        if anadir_formulario.is_valid():
            nuevo_inventario = anadir_formulario.save(commit=False) # Se pone False porque todavía no se hace un commit en la DB.
            nuevo_inventario.save()
            return redirect("/inventario/")
    else:
        anadir_formulario = Anadir()

    return render(request, "inventario/anadir_inventario.html", {"form": anadir_formulario})

@login_required
def borrar_producto(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    inventario.delete()
    return redirect("/inventario/")

@login_required
def actualizar_producto(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        updateForm = Actualizar(data=request.POST)
        if updateForm.is_valid():
            inventario.nombre = updateForm.data['nombre']
            inventario.cantidad = updateForm.data['cantidad']
            inventario.medida = updateForm.data['medida']
            inventario.save()
            return redirect(f"/inventario/per_product/{pk}")

    else:
        updateForm = Actualizar(instance=inventario)
    context = {"form": updateForm}
    return render(request, "inventario/actualizar_inventario.html", context=context)

@login_required
def exportar(request):
    respuesta = HttpResponse(content_type='text/csv')

    writer = csv.writer(respuesta)
    writer.writerow(['Nombre', 'Cantidad', 'Medida']) # "Escribe" el nombre de las columnas

    for articulo in Inventario.objects.all().values_list('nombre', 'cantidad', 'medida'):
        writer.writerow(articulo)

    respuesta['Content-Disposition'] = 'attachment; filename="Inventario.csv' # Identifica el archivo como un "attachment" para descargar

    return respuesta


from django.forms import ModelForm
from .models import Inventario

class Anadir(ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre', 'cantidad', 'medida']

class Actualizar(ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre', 'cantidad', 'medida']
from django import forms
from .models import Carta


class CartaForm(forms.ModelForm):

    class Meta:
        model = Carta
        fields = [
            'nombre',
            'imagen',
            'detalle',
            'nivel',
            'tipos',
        ]
        labels = {
            'nombre': 'Nombre',
            'imagen': 'Image',
            'detalle': 'Detalle',
            'nivel': 'Nivel',
            'tipos': 'Tipos de Carta',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'detalle': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-control'}),
            'tipos': forms.CheckboxSelectMultiple(),
        }

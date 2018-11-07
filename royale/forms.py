from django import forms
from .models import Carta, Tipo, Level


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
            'imagen': 'Imagen Carta',
            'detalle': 'Descripción',
            'nivel': 'Nivel',
            'tipos': 'Tipo de Carta',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(),
            'detalle': forms.Textarea(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-control'}),
            'tipos': forms.CheckboxSelectMultiple(),
        }

class TipoForm(forms.ModelForm):

    class Meta:
        model = Tipo
        fields = [
            'nombre',
            'detalle',
        ]
        labels = {
            'nombre': 'Nombre',
            'imagen': 'Detalle del tipo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Cultivo

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = ['nombre', 'tipo', 'siembra', 'cosecha', 'zona', 'plagas']
        widgets = {
            'plagas': forms.CheckboxSelectMultiple(), # Se ven como varios Checkbox
            'siembra': forms.TextInput(attrs={'placeholder': 'Ej: Agosto'}),
            'cosecha': forms.TextInput(attrs={'placeholder': 'Ej: Diciembre'}),
        }
        labels = {
            'nombre': 'Nombre del cultivo',
            'tipo': 'Tipo de cultivo',
            'siembra': 'Época de siembra',
            'cosecha': 'Época de cosecha',
            'zona': 'Zona asignada',
            'plagas': 'Plagas asociadas'
        }

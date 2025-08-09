from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['clave', 'nombre', 'descripcion', 'nivel', 'duracion_horas', 'costo', 'imagen']  # sin 'creado_en'
        widgets = {
            'clave': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nivel': forms.Select(attrs={'class': 'form-control'}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'costo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

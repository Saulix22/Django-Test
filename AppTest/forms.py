from django import forms
from django.forms import ModelForm
from .models import Material, Solicitud

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        
class SolicitudForm(forms.ModelForm):
    class Meta: 
        model = Solicitud
        fields= ['titulo', 'detalles', 'cantidad']
        
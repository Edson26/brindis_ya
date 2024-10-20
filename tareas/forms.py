from django import forms
from .models import Trabajador, Ingrediente, Receta, Coctel

class FormTrabajador(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'
class FormIngrediente(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = '__all__'
class FormReceta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'
class FormCoctel(forms.ModelForm):
    class Meta:
        model = Coctel
        fields = '__all__'
from django import forms
from .models import Miembros

class MiembrosForm(forms.ModelForm):
    class Meta:
        model = Miembros
        fields = ['nombre', 'apodo', 'contraseña', 'edad', 'color_favorito', 'email']
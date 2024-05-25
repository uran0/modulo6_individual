from django import forms
from .models import Miembros

class MiembrosForm(forms.ModelForm):
    class Meta:
        model = Miembros
        fields = ['nombre', 'apodo', 'edad', 'color_favorito', 'email']
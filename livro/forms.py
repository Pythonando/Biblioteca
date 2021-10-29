from usuarios.models import Usuario
from django import forms
from django.db.models import fields
from .models import Livros, Categoria
from django.db import models    
from datetime import date


class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()

class CategoriaLivro(forms.Form):
    nome = forms.CharField(max_length=30)
    descricao = forms.CharField(max_length=60)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget = forms.Textarea()

        
        



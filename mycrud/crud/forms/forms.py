from cProfile import label
from django import forms

class ProdutoForm(forms.Form):
    nome = forms.CharField(max_length=40, label='Nome')
    preco = forms.FloatField(label='Preço')
    validade = forms.DateField(label='Validade')

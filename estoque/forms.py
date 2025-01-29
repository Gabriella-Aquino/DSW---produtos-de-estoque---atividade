from django import forms
from .models import *

class ProdutoForm(forms.Form):
  nome = forms.CharField(max_length=225, label="Nome:")
  codigo = forms.CharField(max_length=100, label="Codigo:")
  descricao = forms.CharField(label="Descrição:", widget=forms.Textarea())
  preco = forms.DecimalField()
  quantidade_estoque = forms.IntegerField(label="Quantidade:")
  fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all())
  categorias = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all())

class FornecedorForm(forms.Form):
  nome = forms.CharField(max_length=100)
  cnpj = forms.CharField(max_length=14)
  endereco = forms.CharField(max_length=150)

class CategoriaForm(forms.Form):
  nome = forms.CharField(max_length=100)


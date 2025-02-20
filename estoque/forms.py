from django import forms
from .models import *
from django.core.exceptions import ValidationError

class ProdutoForm(forms.Form):
  nome = forms.CharField(max_length=225, label="Nome:")
  codigo = forms.CharField(max_length=100, label="Codigo:")
  descricao = forms.CharField(label="Descrição:", widget=forms.Textarea())
  preco = forms.DecimalField()
  quantidade_estoque = forms.IntegerField(label="Quantidade:")
  fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all())
  categorias = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all())
  imagem = forms.ImageField(label="Imagem do Produto", required=False)

  def clean_preco(self):
    preco = self.cleaned_data.get('preco')
    if not preco > 0:
      raise ValidationError("o preço tem que ser maior que 0")
    return preco
  
  def clean_quantidade_estoque(self):
    quantidade_estoque = self.cleaned_data.get('quantidade_estoque')
    if not isinstance(quantidade_estoque, int):
      raise ValidationError("deve ser um valor inteiro")
    if not quantidade_estoque > 0:
      raise ValidationError("o valor deve ser maior que 0")
    return quantidade_estoque
  
  def clean_codigo(self):
    codigo = self.cleaned_data.get('codigo')
    if not codigo.isalnum():
      raise ValidationError("O codigo não pode ter caracteres diferentes de numero e/ou letras")
    return codigo
  
  def clean_nome(self):
    nome = self.cleaned_data.get('nome')
    if len(nome) < 3:
      raise ValidationError("O nome do produto deve ter pelo menos 3 caracteres.")
    return nome
  

class FornecedorForm(forms.Form):
  nome = forms.CharField(max_length=100)
  cnpj = forms.CharField(max_length=14)
  endereco = forms.CharField(max_length=150)

class CategoriaForm(forms.Form):
  nome = forms.CharField(max_length=100)


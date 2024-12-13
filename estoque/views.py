from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Categoria, Fornecedor, Produto

def index(request):
  produtos = Produto.objects.all()
  categorias = Categoria.objects.all()
  fornecedores = Fornecedor.objects.all()

  context = {
    'produtos': produtos,
    'categorias': categorias,
    'fornecedores': fornecedores,
  }

  return render(request, 'index.html', context)

def detalheProduto(request, id):
  produto = get_object_or_404(Produto, pk=id)
  context = {'produto': produto}
  return render(request, 'detalhe.html', context)

from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponsePermanentRedirect
from django.urls import reverse
from .models import Categoria, Fornecedor, Produto
from .forms import ProdutoForm, FornecedorForm, CategoriaForm

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

def produtoForm(request):
  if request.method == "POST":
    form = ProdutoForm(request.POST)
    if form.is_valid():
      produto = Produto()
      produto.nome = form.cleaned_data['nome']
      produto.codigo = form.cleaned_data['codigo']
      produto.descricao = form.cleaned_data['descricao']
      produto.preco = form.cleaned_data['preco']
      produto.quantidade_estoque = form.cleaned_data['quantidade_estoque']
      produto.fornecedor = form.cleaned_data['fornecedor']
      produto.save()
      produto.categoria.set(form.cleaned_data['categorias'])
      return HttpResponsePermanentRedirect(reverse('index'))
    else:
      form = ProdutoForm(request.post)
  else:
    form = ProdutoForm()
  return render(request, "cadastro.html", {'form': form})


def fornecedorForm(request):
  if request.method == "POST":
    form = FornecedorForm(request.POST)
    if form.is_valid():
      fornecedor = Fornecedor()
      fornecedor.nome = form.cleaned_data['nome']
      fornecedor.cnpj = form.cleaned_data['cnpj']
      fornecedor.endereco = form.cleaned_data['endereco']
      fornecedor.save()
      return HttpResponsePermanentRedirect(reverse('index'))
    else:
      form = FornecedorForm(request.post)
  else:
    form = FornecedorForm()
  return render(request, 'cadastro.html', {'form': form})

def categoriaForm(request):
  if request.method == 'POST':
    form = CategoriaForm(request.POST)
    if form.is_valid():
      categoria = Categoria()
      categoria.nome = form.cleaned_data['nome']
      categoria.save()
      return HttpResponsePermanentRedirect(reverse('index'))
    else:
      form = CategoriaForm(request.POST)
  else:
    form = CategoriaForm()

  return render(request, 'cadastro.html', {'form' : form})
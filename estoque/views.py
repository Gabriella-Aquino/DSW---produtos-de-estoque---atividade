from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponsePermanentRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from .models import Categoria, Fornecedor, Produto
from .forms import ProdutoForm, FornecedorForm, CategoriaForm

class IndexView(ListView):
  model = Produto
  template_name = "index.html"
  context_object_name = "produtos"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["categorias"] = Categoria.objects.all()
    context["fornecedores"] = Fornecedor.objects.all()
    return context

# def index(request):
#   produtos = Produto.objects.all()
#   categorias = Categoria.objects.all()
#   fornecedores = Fornecedor.objects.all()

#   context = {
#     'produtos': produtos,
#     'categorias': categorias,
#     'fornecedores': fornecedores,
#   }

#   return render(request, 'index.html', context)


class DetalheProdutoView(DetailView):
  model = Produto
  template_name = 'detalhe.html'
  context_object_name = 'produto'

# def detalheProduto(request, id):
#   produto = get_object_or_404(Produto, pk=id)
#   context = {'produto': produto}
#   return render(request, 'detalhe.html', context)


class ProdutoFormView(FormView):
  template_name = 'cadastro.html'
  form_class = ProdutoForm
  success_url = reverse_lazy('index')

  def form_valid(self, form):
    produto = Produto(
      nome = form.cleaned_data['nome'],
      codigo = form.cleaned_data['codigo'],
      descricao = form.cleaned_data['descricao'],
      preco = form.cleaned_data['preco'],
      quantidade_estoque = form.cleaned_data['quantidade_estoque'],
      fornecedor = form.cleaned_data['fornecedor'],
    )
    produto.save()
    produto.categoria.set(form.cleaned_data['categorias'])
    return super().form_valid(form)

# def produtoForm(request):
#   if request.method == "POST":
#     form = ProdutoForm(request.POST)
#     if form.is_valid():
#       produto = Produto()
#       produto.nome = form.cleaned_data['nome']
#       produto.codigo = form.cleaned_data['codigo']
#       produto.descricao = form.cleaned_data['descricao']
#       produto.preco = form.cleaned_data['preco']
#       produto.quantidade_estoque = form.cleaned_data['quantidade_estoque']
#       produto.fornecedor = form.cleaned_data['fornecedor']
#       produto.save()
#       produto.categoria.set(form.cleaned_data['categorias'])
#       return HttpResponsePermanentRedirect(reverse('index'))
#     else:
#       form = ProdutoForm(request.POST)
#   else:
#     form = ProdutoForm()
#   return render(request, "cadastro.html", {'form': form})


class FornecedorFormView(FormView):
  template_name = 'cadastro.html'
  form_class = FornecedorForm
  success_url = reverse_lazy('index')

  def form_valid(self, form):
    fornecedor = Fornecedor()
    fornecedor.nome = form.cleaned_data['nome']
    fornecedor.cnpj = form.cleaned_data['cnpj']
    fornecedor.endereco = form.cleaned_data['endereco']
    fornecedor.save()
    return super().form_valid(form)

# def fornecedorForm(request):
#   if request.method == "POST":
#     form = FornecedorForm(request.POST)
#     if form.is_valid():
#       fornecedor = Fornecedor()
#       fornecedor.nome = form.cleaned_data['nome']
#       fornecedor.cnpj = form.cleaned_data['cnpj']
#       fornecedor.endereco = form.cleaned_data['endereco']
#       fornecedor.save()
#       return HttpResponsePermanentRedirect(reverse('index'))
#     else:
#       form = FornecedorForm(request.POST)
#   else:
#     form = FornecedorForm()
#   return render(request, 'cadastro.html', {'form': form})


class CategoriaFormView(FormView):
  template_name = 'cadastro.html'
  form_class = CategoriaForm
  success_url = reverse_lazy('index')

  def form_valid(self, form):
    categoria = Categoria()
    categoria.nome = form.cleaned_data['nome']
    categoria.save()

    return super().form_valid(form)

# def categoriaForm(request):
#   if request.method == 'POST':
#     form = CategoriaForm(request.POST)
#     if form.is_valid():
#       categoria = Categoria()
#       categoria.nome = form.cleaned_data['nome']
#       categoria.save()
#       return HttpResponsePermanentRedirect(reverse('index'))
#     else:
#       form = CategoriaForm(request.POST)
#   else:
#     form = CategoriaForm()

#   return render(request, 'cadastro.html', {'form' : form})
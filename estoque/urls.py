from django.urls import path
from .views import IndexView, DetalheProdutoView, ProdutoFormView, FornecedorFormView, CategoriaFormView
#from .views import index, detalheProduto, produtoForm, fornecedorForm, categoriaForm


urlpatterns = [
    path('', IndexView.as_view() ,name='index'),
    path('detalhes-produto/<int:pk>/', DetalheProdutoView.as_view(), name='detalhe-produto'),
    path('cadastrar-produto/', ProdutoFormView.as_view(), name='cadastrar-produto'),
    path('cadastrar-fornecedor/', FornecedorFormView.as_view(), name='cadastrar-fornecedor'),
    path('cadastrar-categoria/', CategoriaFormView.as_view(), name='cadastrar-categoria'),
]

# urlpatterns = [
#     path('', index ,name='index'),
#     path('detalhes-produto/<int:id>/', detalheProduto, name='detalhe-produto'),
#     path('cadastrar-produto/', produtoForm, name='cadastrar-produto'),
#     path('cadastrar-fornecedor/', fornecedorForm, name='cadastrar-fornecedor'),
#     path('cadastrar-categoria/', categoriaForm, name='cadastrar-categoria'),
# ]
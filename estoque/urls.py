from django.urls import path
from .views import index, detalheProduto, produtoForm, fornecedorForm, categoriaForm

urlpatterns = [
    path('', index ,name='index'),
    path('detalhes-produto/<int:id>/', detalheProduto, name='detalhe-produto'),
    path('cadastrar-produto/', produtoForm, name='cadastrar-produto'),
    path('cadastrar-fornecedor/', fornecedorForm, name='cadastrar-fornecedor'),
    path('cadastrar-categoria/', categoriaForm, name='cadastrar-categoria'),
]
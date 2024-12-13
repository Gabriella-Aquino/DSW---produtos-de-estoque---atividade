from django.urls import path
from .views import index, detalheProduto

urlpatterns = [
    path('', index ,name='index'),
    path('detalhes-produto/<int:id>/', detalheProduto, name='detalhe-produto')
]
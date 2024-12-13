from django.contrib import admin
from .models import Produto

admin.site.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'preco', 'quantidade_estoque', 'data_criacao')
    search_fields = ('codigo', 'nome')  
    list_filter = ('data_criacao',)  
    ordering = ('-data_criacao',)


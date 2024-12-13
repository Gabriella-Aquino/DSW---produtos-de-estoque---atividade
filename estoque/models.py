from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255 )
    codigo = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"



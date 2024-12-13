from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nome}"
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"

class Produto(models.Model):
    nome = models.CharField(max_length=255 )
    codigo = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"



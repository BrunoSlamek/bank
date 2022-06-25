from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ativo(models.Model):

    MODADLIDADE = [
        ('RF', 'Renda Fixa'),
        ('RV', 'Renda Variavel'),
        ('CP', 'Cripto'),
        ('FI', 'Fundo Imobiliário'),
    ]

    nome = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=2, choices=MODADLIDADE)
    created_by = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Carteira(models.Model):
    nome = models.CharField(max_length=100)
    saldo = models.IntegerField(default=0)
    qtd_aplicacoes = models.IntegerField(default=0)
    qtd_venda = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, default=User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class Aplicacao(models.Model):
    OPERACAO = [
        ('C', 'Compra'),
        ('V', 'Venda'),
    ]

    operacao = models.CharField(max_length=1, choices=OPERACAO)
    carteira = models.ForeignKey(Carteira, on_delete=models.DO_NOTHING)
    ativo = models.ForeignKey(Ativo, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    valor = models.IntegerField()
    data_compra = models.DateField()
    created_by = models.ForeignKey(User, default=User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

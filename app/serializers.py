from rest_framework import serializers
from .models import Ativo, Carteira, Aplicacao
from typing import List
from django.contrib.auth.models import User


class AtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model: str = Ativo
        fields: List[str] = ['nome', 'modalidade']


class CarteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model: str = Carteira
        fields: List[str] = ['nome', 'saldo']


class AplicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model: str = Aplicacao
        fields: List[str] = ['operacao', 'ativo', 'quantidade', 'valor', 'data_compra']

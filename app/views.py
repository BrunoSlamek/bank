from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import AtivoSerializer, CarteiraSerializer, AplicacaoSerializer
from .models import Ativo, Carteira, Aplicacao
from django.contrib.auth.models import User
import django_filters.rest_framework


class AtivoViewSet(viewsets.ModelViewSet):
    queryset = Ativo.objects.all()
    serializer_class = AtivoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    # create ativo
    def create(self, request, *args, **kwargs):
        serializer = AtivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)


class CarteiraViewSet(viewsets.ModelViewSet):
    queryset = Carteira.objects.all()
    serializer_class = CarteiraSerializer

    def list(self, request):
        queryset = Carteira.objects.filter(created_by=request.user.id)
        serializer = CarteiraSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CarteiraSerializer(data=request.data)
        if not Carteira.objects.filter(created_by=request.user.id).exists():
            if serializer.is_valid():
                serializer.save(created_by=request.user)
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({"error": "You can't create more than one carteira"})


class AplicacaoViewSet(viewsets.ModelViewSet):
    queryset = Aplicacao.objects.all()
    serializer_class = AplicacaoSerializer

    def list(self, request, *args, **kwargs):
        queryset = Aplicacao.objects.filter(created_by=request.user.id)
        serializer = AplicacaoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AplicacaoSerializer(data=request.data)
        if serializer.is_valid():
            carteira_user = Carteira.objects.get(created_by=request.user.id)
            print(carteira_user.id)
            if serializer.validated_data['operacao'] == 'C':
                Carteira.objects.update(
                    id=carteira_user.id,
                    saldo=carteira_user.saldo + serializer.validated_data['valor'],
                    qtd_aplicacoes=carteira_user.qtd_aplicacoes + 1
                )
            else:
                Carteira.objects.update(
                    id=carteira_user.id,
                    saldo=carteira_user.saldo - serializer.validated_data['valor'],
                    qtd_venda=carteira_user.qtd_venda + 1
                ) 
            serializer.save(carteira_id=carteira_user.id, created_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

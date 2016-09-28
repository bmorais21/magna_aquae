# coding: utf-8

from rbcapp.models import Bacia_Hidrografica, Rio, Ponto_Monitoramento, Coleta, Monitoramento
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers

class Monitoramento_Localizacao(View):
    
    def get(self, request):
        bacia_hidrografica = Bacia_Hidrografica.objects.all()
        return render(request, 'monitoramento/localizacao.html', {'bacia_hidrografica':bacia_hidrografica})
    
    def post(self, request):
        if 'bacia' in request.POST:
            id = request.POST['bacia']
            rios = Rio.objects.filter(bacia_hidrografica=id)
            json = serializers.serialize("json", rios)
            return HttpResponse(json)
        elif 'rio' in request.POST:
            id = request.POST['rio']
            pontos = Ponto_Monitoramento.objects.filter(rio=id)
            json = serializers.serialize("json", pontos)
            return HttpResponse(json)
        elif 'ponto' in request.POST:
            id = request.POST['ponto']
            datas = Monitoramento.objects.filter(ponto_monitoramento=id)
            json = serializers.serialize("json", datas)
            return HttpResponse(json)
        return HttpResponse()
        

class Monitoramento_Imagem(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass

class Monitoramento_Entorno(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass

class Monitoramento_Caso(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass
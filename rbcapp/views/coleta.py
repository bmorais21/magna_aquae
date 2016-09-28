# coding: utf-8

from rbcapp.models import Coleta, Substancia, Ponto_Monitoramento, Monitoramento, Rio, Bacia_Hidrografica, \
    Coleta_Substancia
from rbcapp.forms.coleta import FormColeta
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers


class Coleta_Listar(View):
    template = 'coleta/index.html'
    
    def get(self, request):
        coletas = Coleta.objects.all()
        col = []
        for coleta in coletas:
            sbs = {}
            ponto = Ponto_Monitoramento.objects.get(id=coleta.ponto_monitoramento.id)
            sbs['ponto_monitoramento'] = ponto
            sbs['data_coleta'] = coleta.data_coleta
            sbs['id'] = coleta.id
            rio = Rio.objects.get(id=ponto.rio.id)
            sbs['rio'] = rio.nome
            col.append(sbs)
        
        return render(request, self.template, {'coletas': col})
    
    def post(self, request):
        coletas = Coleta.objects.all()
        return render(request, self.template, {'dados': coletas})


class Coleta_Info(View):
    template = 'coleta/info.html'
    
    def get(self, request):
        coleta = Coleta.objects.get(id=request.GET['id'])
        coleta_substancia = Coleta_Substancia.objects.filter(coleta=coleta)
        return render(request, self.template, {'coleta': coleta, 'coleta_substancia': coleta_substancia})


class Coleta_Add(View):
    template = 'coleta/'
    
    def get(self, request):
        if 'bh' in request.GET:
            id = request.GET['bh']
            rios = Rio.objects.filter(bacia_hidrografica=id)
            json = serializers.serialize("json", rios)
            return HttpResponse(json)
        elif 'rio' in request.GET:
            id = request.GET['rio']
            pontos = Ponto_Monitoramento.objects.filter(rio=id)
            json = serializers.serialize("json", pontos)
            return HttpResponse(json)
        self.template += 'add.html'
        form = FormColeta()
        return render(request, self.template,
                      {'form': form, 'bhs': Bacia_Hidrografica.objects.all(), 'substancias': Substancia.objects.all()})
    
    def post(self, request):
        template = '/coleta/'
        form = FormColeta(request.POST)
        if form.is_valid():
            substancias = request.POST.getlist('substancia')
            valores_coletados = request.POST.getlist('valor_coletado')
            
            coleta = Coleta()
            coleta.data_coleta = request.POST['data_coleta']
            coleta.ponto_monitoramento = Ponto_Monitoramento.objects.get(pk=request.POST['ponto'])
            coleta.save()
            
            for i in range(len(substancias)):
                coleta_substancia = Coleta_Substancia()
                coleta_substancia.coleta = Coleta.objects.get(pk=coleta.id)
                coleta_substancia.substancia = Substancia.objects.get(pk=substancias[i])
                coleta_substancia.valor_coletado = float(valores_coletados[i])
                coleta_substancia.save()
        
        return redirect(template)
        
        # class Coleta_Delete(View):
        #     template = '/coleta/'
        #     def get(self, request, coleta_id=None):
        #         coleta = Coleta.objects.get(pk=coleta_id)
        #         if coleta.id != None:
        #             coleta.delete()
        #         return redirect(self.template)
        #
        #     def post(self, request, coleta_id=None):
        #         coleta = Coleta.objects.get(pk=coleta_id)
        #         if coleta.id != None:
        #             coleta.delete()
        #         return redirect(self.template)

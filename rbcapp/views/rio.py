# coding: utf-8

from rbcapp.models import Rio, Bacia_Hidrografica
from rbcapp.forms.rio import FormRio
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers

class Rio_Listar(View):
    template = 'rio/index.html'

    def get(self, request):
        rios = Rio.objects.all()
        bhs = Bacia_Hidrografica.objects.all()
        return render(request, self.template, {'dados': rios, 'bhs': bhs})

    def post(self, request):
        bh = request.POST['bh']
        if bh == 'selecione':
            rios = Rio.objects.all()
            json = serializers.serialize("json", rios)
        else:
            rios = Rio.objects.filter(bacia_hidrografica=bh)
            json = serializers.serialize("json", rios)
        return HttpResponse(json)


class Rio_Add(View):
    template = 'rio/'

    def get(self, request):
        self.template += 'add.html'
        form = FormRio()
        return render(request, self.template, {'form': form})

    def post(self, request):
        template = '/rio/'
        form = FormRio(request.POST)
        if form.is_valid():
            rio = Rio()
            rio.nome = request.POST['nome']
            rio.dimensao = request.POST['dimensao']
            rio.bacia_hidrografica = Bacia_Hidrografica.objects.get(pk=request.POST['bacia_hidrografica'])
            rio.save()
        return redirect(template)

class Rio_Edit(View):
    template = 'rio/'

    def get(self, request, rio_id=None):
        self.template += 'edit.html/'
        rio = Rio.objects.get(pk=rio_id)
        form = FormRio(initial={'nome': rio.nome, 'dimensao': rio.dimensao, 'bacia_hidrografica': rio.bacia_hidrografica})
        return render(request, self.template, {'form': form, 'rio_id': rio.id})

    def post(self, request, rio_id=None):
        template = '/rio/'
        rio = Rio.objects.get(pk=rio_id)
        form = FormRio(request.POST)
        if form.is_valid():
            rio.nome = request.POST['nome']
            rio.dimensao = request.POST['dimensao']
            rio.bacia_hidrografica = Bacia_Hidrografica.objects.get(pk=request.POST['bacia_hidrografica'])
            rio.save()
        return redirect(template)

class Rio_Delete(View):
    template = '/rio/'
    def get(self, request, rio_id=None):
        rio = Rio.objects.get(pk=rio_id)
        if rio.id != None:
            rio.delete()
        return redirect(self.template)

    def post(self, request, rio_id=None):
        rio = Rio.objects.get(pk=rio_id)
        if rio.id != None:
            rio.delete()
        return redirect(self.template)

# coding: utf-8

from rbcapp.models import Ponto_Monitoramento, Rio, Bacia_Hidrografica
from rbcapp.forms.ponto import FormPonto
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers

class Ponto_Listar(View):
    template = 'ponto/index.html'

    def get(self, request):
        rios = Rio.objects.all()
        return render(request, self.template, {'rios': rios})

    def post(self, request):
        id = request.POST['ponto']
        pontos = Ponto_Monitoramento.objects.filter(rio=id)
        json = serializers.serialize("json", pontos)
        return HttpResponse(json)

class Ponto_Add(View):
    template = 'ponto/'

    def get(self, request):
        if 'bh' in request.GET:
            id = request.GET['bh']
            rios = Rio.objects.filter(bacia_hidrografica=id)
            json = serializers.serialize("json", rios)
            return HttpResponse(json)
        self.template += 'add.html'
        form = FormPonto()
        bhs = Bacia_Hidrografica.objects.all()
        return render(request, self.template, {'form': form, 'bhs': bhs})

    def post(self, request):
        template = '/ponto/'
        form = FormPonto(request.POST)
        if form.is_valid():
            ponto = Ponto_Monitoramento()
            ponto.latitude = request.POST['latitude']
            ponto.longitude = request.POST['longitude']
            ponto.rio = Rio.objects.get(pk=request.POST['rio'])
            ponto.save()
        return redirect(template)

class Ponto_Edit(View):
    template = 'ponto/'

    def get(self, request, ponto_id=None):
        self.template += 'edit.html/'
        ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)
        form = FormPonto(initial={'latitude': ponto.latitude, 'longitude': ponto.longitude, 'rio': ponto.rio})
        return render(request, self.template, {'form': form, 'ponto_id': ponto.id})

    def post(self, request, ponto_id=None):
        template = '/ponto/'
        ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)
        form = FormPonto(request.POST)
        if form.is_valid():
            ponto.latitude = request.POST['latitude']
            ponto.longitude = request.POST['longitude']
            ponto.rio = Rio.objects.get(pk=request.POST['rio'])
            ponto.save()
        return redirect(template)

class Ponto_Delete(View):
    template = '/ponto/'

    def get(self, request, ponto_id=None):
        ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)
        if ponto.id != None:
            ponto.delete()
        return redirect(self.template)

    def post(self, request, ponto_id=None):
        ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)
        if ponto.id != None:
            ponto.delete()
        return redirect(self.template)

# coding: utf-8

from rbcapp.models import Bacia_Hidrografica
from rbcapp.forms.bacia_hidrografica import FormBaciaHidrografica
from django.shortcuts import render, redirect
from django.views.generic.base import View

class Bacia_Hidrografica_Listar(View):
    template = 'bacia-hidrografica/index.html'
    def get(self, request):
        bh = Bacia_Hidrografica.objects.all()
        return render(request, self.template, {'dados': bh})

    def post(self, request):
        bh = Bacia_Hidrografica.objects.all()
        return render(request, self.template, {'dados': bh})

class Bacia_Hidrografica_Add(View):
    template = 'bacia-hidrografica/'
    def get(self, request):
        self.template += 'add.html'
        form = FormBaciaHidrografica()
        return render(request, self.template, {'form':form})

    def post(self, request):
        template = '/bacia-hidrografica/'
        form = FormBaciaHidrografica(request.POST)
        if form.is_valid():
            bh = Bacia_Hidrografica()
            bh.nome = request.POST['nome']
            bh.save()
        return redirect(template)

class Bacia_Hidrografica_Edit(View):
    template = 'bacia-hidrografica/'
    def get(self, request, bh_id=None):
        self.template += 'edit.html/'
        bh = Bacia_Hidrografica.objects.get(pk=bh_id)
        form = FormBaciaHidrografica(initial={'nome': bh.nome})
        return render(request, self.template, {'form': form, 'bh_id': bh.id})

    def post(self, request, bh_id=None):
        template = '/bacia-hidrografica/'
        bh = Bacia_Hidrografica.objects.get(pk=bh_id)
        form = FormBaciaHidrografica(request.POST)
        if form.is_valid():
            bh.nome = request.POST['nome']
            bh.save()
        return redirect(template)

class Bacia_Hidrografica_Delete(View):
    template = '/bacia-hidrografica/'
    def get(self, request, bh_id=None):
        bh = Bacia_Hidrografica.objects.get(pk=bh_id)
        if bh.id != None:
            bh.delete()
        return redirect(self.template)

    def post(self, request, bh_id=None):
        bh = Bacia_Hidrografica.objects.get(pk=bh_id)
        if bh.id != None:
            bh.delete()
        return redirect(self.template)

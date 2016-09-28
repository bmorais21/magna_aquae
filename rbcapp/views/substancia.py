# coding: utf-8

from rbcapp.forms.substancia import FormSubstancia
from rbcapp.models import Substancia
from django.shortcuts import render, redirect
from django.views.generic.base import View

class Substancia_Listar(View):
    template = 'substancia/index.html'

    def get(self, request):
        substancias = Substancia.objects.all()
        return render(request, self.template, {'dados': substancias})

    def post(self, request):
        substancias = Substancia.objects.all()
        return render(request, self.template, {'dados': substancias})

class Substancia_Add(View):
    template = 'substancia/'

    def get(self, request):
        self.template += 'add.html'
        form = FormSubstancia()
        return render(request, self.template, {'form': form})

    def post(self, request):
        template = '/substancia/'
        form = FormSubstancia(request.POST)
        if form.is_valid():
            substancia = Substancia()
            substancia.nome = request.POST['nome']
            substancia.save()
        return redirect(template)

class Substancia_Edit(View):
    template = 'substancia/'

    def get(self, request, substancia_id=None):
        self.template += 'edit.html/'
        substancia = Substancia.objects.get(pk=substancia_id)
        form = FormSubstancia(initial={'nome': substancia.nome})
        return render(request, self.template, {'form': form, 'substancia_id': substancia.id})

    def post(self, request, substancia_id=None):
        template = '/substancia/'
        substancia = Substancia.objects.get(pk=substancia_id)
        form = FormSubstancia(request.POST)
        if form.is_valid():
            substancia.nome = request.POST['nome']
            substancia.save()
        return redirect(template)

class Substancia_Delete(View):
    template = '/substancia/'
    def get(self, request, substancia_id=None):
        substancia = Substancia.objects.get(pk=substancia_id)
        if substancia.id != None:
            substancia.delete()
        return redirect(self.template)

    def post(self, request, substancia_id=None):
        substancia = Substancia.objects.get(pk=substancia_id)
        if substancia.id != None:
            substancia.delete()
        return redirect(self.template)
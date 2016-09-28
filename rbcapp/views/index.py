# coding: utf-8

from django.shortcuts import render
from django.views.generic.base import View

# def home(request):
#     return render(request, 'base.html')

class Index(View):
    def get(self, request):
        return render(request, 'base.html')
    def post(self, request):
        return render(request, 'base.html')
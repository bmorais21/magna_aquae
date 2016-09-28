#coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


class Cadastrar_Usuario(View):
    
    def get(self, request):
        template = 'user/cadastro.html'
        return render(request, template)
    
    def post(self, request):
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        login = request.POST['login']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        if senha == senha2:
            user = User.objects.create_user(login, email, senha)
            user.first_name = nome
            user.last_name = sobrenome
            user.email = email
            user.save()
            return redirect('index')
        else:
            pass
    
class Login_Usuario(View):
    
    def get(self, request):
        template = 'user/login.html'
        return render(request, template)
    
    def post(self, request):
        login = request.POST['login']
        senha = request.POST['senha']
        user = authenticate(username=login, password=senha)
        if user is not None:
            from django.contrib.auth import login
            login(request, user)
            return redirect('index')
        else:
            pass

class Logout_Usuario(View):
    
    def get(self, request):
        logout(request)
        return redirect('index')
    
    def post(self, request):
        pass
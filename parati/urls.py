"""tcc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rbcapp.views import Index, Cadastrar_Usuario, Login_Usuario, Logout_Usuario, Bacia_Hidrografica_Listar, \
Bacia_Hidrografica_Add, Bacia_Hidrografica_Edit, Bacia_Hidrografica_Delete, Rio_Listar, Rio_Add, Rio_Edit, Rio_Delete, \
Ponto_Listar, Ponto_Add, Ponto_Edit, Ponto_Delete, Coleta_Listar, Coleta_Add, Coleta_Info, Entorno_Listar, Entorno_Add, \
Entorno_Delete, Caso_Listar, Caso_Add, Caso_Edit, Caso_Delete, Monitoramento_Localizacao, Caso_Pesquisar


urlpatterns = [
    
    url("^admin/", include(admin.site.urls)),
    
    #Home
    url(r'^$', Index.as_view(), name='index'),
    url(r'^login/$', Login_Usuario.as_view(), name='login'),
    url(r'^logout/$', Logout_Usuario.as_view(), name='logout'),
    url(r'^cadastro/$', Cadastrar_Usuario.as_view(), name='cadastro_usuario'),
    
    #Bacia Hidrografica
    url(r'^bacia-hidrografica/$', Bacia_Hidrografica_Listar.as_view(), name='bacia_hidrografica_listar'),
    url(r'^bacia-hidrografica/add/$', Bacia_Hidrografica_Add.as_view(), name='bacia_hidrografica_add'),
    url(r'^bacia-hidrografica/edit/(?P<bh_id>\d+)/$', Bacia_Hidrografica_Edit.as_view(), name='bacia_hidrografica_edit'),
    url(r'^bacia-hidrografica/delete/(?P<bh_id>\d+)$', Bacia_Hidrografica_Delete.as_view(), name='bacia_hidrografica_delete'),

    #Rio
    url(r'^rio/$', Rio_Listar.as_view(), name='rio_listar'),
    url(r'^rio/add/$', Rio_Add.as_view(), name='rio_add'),
    url(r'^rio/edit/(?P<rio_id>\d+)/$', Rio_Edit.as_view(), name='rio_edit'),
    url(r'^rio/delete/(?P<rio_id>\d+)/$', Rio_Delete.as_view(), name='rio_delete'),

    #Ponto
    url(r'^ponto/$', Ponto_Listar.as_view(), name='ponto_listar'),
    url(r'^ponto/add/$', Ponto_Add.as_view(), name='ponto_add'),
    url(r'^ponto/edit/(?P<ponto_id>\d+)/$', Ponto_Edit.as_view(), name='ponto_edit'),
    url(r'^ponto/delete/(?P<ponto_id>\d+)/$', Ponto_Delete.as_view(), name='ponto_delete'),

    #Substancia
    # url(r'^substancia/$', Substancia_Listar.as_view()),
    # url(r'^substancia/add/$', Substancia_Add.as_view()),
    # url(r'^substancia/edit/(?P<substancia_id>\d+)/$', Substancia_Edit.as_view()),
    # url(r'^substancia/delete/(?P<substancia_id>\d+)/$', Substancia_Delete.as_view()),

    #Coleta
    url(r'^coleta/$', Coleta_Listar.as_view(), name='coleta_listar'),
    url(r'^coleta/add/$', Coleta_Add.as_view(), name='coleta_add'),
    url(r'^coleta/info/$', Coleta_Info.as_view(), name='coleta_info'),
    # url(r'^coleta/delete/(?P<coleta_id>\d+)/$', Coleta_Delete.as_view()),

    #Entorno
    url(r'^entorno/$', Entorno_Listar.as_view(), name='entorno_listar'),
    url(r'^entorno/add/$', Entorno_Add.as_view(), name='entorno_add'),
    # url(r'^entorno/edit/(?P<entorno_id>\d+)/$', Entorno_Edit.as_view()),
    url(r'^entorno/delete/(?P<entorno_id>\d+)/$', Entorno_Delete.as_view(), name='entorno_delete'),

    #Caso
    url(r'^caso/$', Caso_Listar.as_view(), name='caso_listar'),
    url(r'^caso/add/$', Caso_Add.as_view(), name='caso_add'),
    url(r'^caso/edit/(?P<caso_id>\d+)/$', Caso_Edit.as_view(), name='caso_edit'),
    url(r'^caso/delete/(?P<caso_id>\d+)/$', Caso_Delete.as_view(), name='caso_delete'),
    url(r'^caso/pesquisar/$', Caso_Pesquisar.as_view(), name='caso_pesquisar'),
    
    #Monitoramento
    url(r'^monitoramento/$', Monitoramento_Localizacao.as_view(), name='monitoramento_localizacao'),

]

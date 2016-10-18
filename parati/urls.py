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
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    url("^admin/", include(admin.site.urls)),
    
    #Home
    url(r'^$', Index.as_view(), name='index'),
    url(r'^login/$', Login_Usuario.as_view(), name='login'),
    url(r'^logout/$', Logout_Usuario.as_view(), name='logout'),
    url(r'^cadastro/$', Cadastrar_Usuario.as_view(), name='cadastro_usuario'),
    
    #Bacia Hidrografica
    url(r'^bacia-hidrografica/$', login_required(Bacia_Hidrografica_Listar.as_view(), login_url='/login/'), name='bacia_hidrografica_listar'),
    url(r'^bacia-hidrografica/add/$', login_required(Bacia_Hidrografica_Add.as_view(), login_url='/login/'), name='bacia_hidrografica_add'),
    url(r'^bacia-hidrografica/edit/(?P<bh_id>\d+)/$', login_required(Bacia_Hidrografica_Edit.as_view(), login_url='/login/'), name='bacia_hidrografica_edit'),
    url(r'^bacia-hidrografica/delete/(?P<bh_id>\d+)$', login_required(Bacia_Hidrografica_Delete.as_view(), login_url='/login/'), name='bacia_hidrografica_delete'),

    #Rio
    url(r'^rio/$', login_required(Rio_Listar.as_view(), login_url='/login/'), name='rio_listar'),
    url(r'^rio/add/$', login_required(Rio_Add.as_view(), login_url='/login/'), name='rio_add'),
    url(r'^rio/edit/(?P<rio_id>\d+)/$', login_required(Rio_Edit.as_view(), login_url='/login/'), name='rio_edit'),
    url(r'^rio/delete/(?P<rio_id>\d+)/$', login_required(Rio_Delete.as_view(), login_url='/login/'), name='rio_delete'),

    #Ponto
    url(r'^ponto/$', login_required(Ponto_Listar.as_view(), login_url='/login/'), name='ponto_listar'),
    url(r'^ponto/add/$', login_required(Ponto_Add.as_view(), login_url='/login/'), name='ponto_add'),
    url(r'^ponto/edit/(?P<ponto_id>\d+)/$', login_required(Ponto_Edit.as_view(), login_url='/login/'), name='ponto_edit'),
    url(r'^ponto/delete/(?P<ponto_id>\d+)/$', login_required(Ponto_Delete.as_view(), login_url='/login/'), name='ponto_delete'),

    #Substancia
    # url(r'^substancia/$', Substancia_Listar.as_view()),
    # url(r'^substancia/add/$', Substancia_Add.as_view()),
    # url(r'^substancia/edit/(?P<substancia_id>\d+)/$', Substancia_Edit.as_view()),
    # url(r'^substancia/delete/(?P<substancia_id>\d+)/$', Substancia_Delete.as_view()),

    #Coleta
    url(r'^coleta/$', login_required(Coleta_Listar.as_view(), login_url='/login/'), name='coleta_listar'),
    url(r'^coleta/add/$', login_required(Coleta_Add.as_view(), login_url='/login/'), name='coleta_add'),
    url(r'^coleta/info/$', login_required(Coleta_Info.as_view(), login_url='/login/'), name='coleta_info'),
    # url(r'^coleta/delete/(?P<coleta_id>\d+)/$', Coleta_Delete.as_view()),

    #Entorno
    url(r'^entorno/$', login_required(Entorno_Listar.as_view(), login_url='/login/'), name='entorno_listar'),
    url(r'^entorno/add/$', login_required(Entorno_Add.as_view(), login_url='/login/'), name='entorno_add'),
    # url(r'^entorno/edit/(?P<entorno_id>\d+)/$', Entorno_Edit.as_view()),
    url(r'^entorno/delete/(?P<entorno_id>\d+)/$', login_required(Entorno_Delete.as_view(), login_url='/login/'), name='entorno_delete'),

    #Caso
    url(r'^caso/$', login_required(Caso_Listar.as_view(), login_url='/login/'), name='caso_listar'),
    url(r'^caso/add/$', login_required(Caso_Add.as_view(), login_url='/login/'), name='caso_add'),
    url(r'^caso/edit/(?P<caso_id>\d+)/$', login_required(Caso_Edit.as_view(), login_url='/login/'), name='caso_edit'),
    url(r'^caso/delete/(?P<caso_id>\d+)/$', login_required(Caso_Delete.as_view(), login_url='/login/'), name='caso_delete'),
    url(r'^caso/pesquisar/$', login_required(Caso_Pesquisar.as_view(), login_url='/login/'), name='caso_pesquisar'),
    
    #Monitoramento
    url(r'^monitoramento/$', login_required(Monitoramento_Localizacao.as_view(), login_url='/login/'), name='monitoramento_localizacao'),

]

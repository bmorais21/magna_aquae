from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from index import Index
from user import Cadastrar_Usuario, Login_Usuario, Logout_Usuario
from bacia_hidrografica import Bacia_Hidrografica_Listar, Bacia_Hidrografica_Add, Bacia_Hidrografica_Edit, Bacia_Hidrografica_Delete
from rio import Rio_Listar, Rio_Add, Rio_Edit, Rio_Delete
from ponto import Ponto_Listar, Ponto_Add, Ponto_Edit, Ponto_Delete
from substancia import Substancia_Listar, Substancia_Add, Substancia_Edit, Substancia_Delete
from coleta import Coleta_Listar, Coleta_Add, Coleta_Info
from entorno import Entorno_Listar, Entorno_Add, Entorno_Edit, Entorno_Delete
from caso import Caso_Listar, Caso_Add, Caso_Edit, Caso_Delete, Caso_Pesquisar
from monitoramento import Monitoramento_Localizacao, Monitoramento_Imagem, Monitoramento_Entorno, Monitoramento_Caso

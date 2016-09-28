# coding: utf-8

from django.db import models
from bacia_hidrografica import Bacia_Hidrografica
from rio import Rio
from ponto_monitoramento import Ponto_Monitoramento
from monitoramento import Monitoramento
from casos import Casos

class Historico_Monitoramento(models.Model):
	bacia = models.ForeignKey(Bacia_Hidrografica)
	rio = models.ForeignKey(Rio)
	ponto_monitoramento = models.ForeignKey(Ponto_Monitoramento)
	monitoramento = models.ForeignKey(Monitoramento)
	solucao = models.ForeignKey(Casos)
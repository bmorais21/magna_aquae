from django.contrib import admin
from models.bacia_hidrografica import Bacia_Hidrografica
from models.coleta import Coleta
from models.entorno import Entorno
from models.monitoramento import Monitoramento
from models.ponto_monitoramento import Ponto_Monitoramento
from models.rio import Rio
from models.substancia import Substancia
from models.casos import Casos
from models.coleta_substancia import Coleta_Substancia
# from historico import Historico_Monitoramento

# Register your models here.
admin.site.register(Bacia_Hidrografica)
admin.site.register(Coleta)
admin.site.register(Entorno)
admin.site.register(Monitoramento)
admin.site.register(Ponto_Monitoramento)
admin.site.register(Rio)
admin.site.register(Substancia)
admin.site.register(Casos)
admin.site.register(Coleta_Substancia)
# admin.site.register(Historico_Monitoramento)
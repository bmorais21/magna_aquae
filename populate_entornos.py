# coding: utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parati.settings')

import django

django.setup()

import rbcapp.models.entorno


def populate():

    add_entorno(variavel_entorno="Vegetação", cor_hex="#033403", cor_rgb="(3,52,3)")
    add_entorno(variavel_entorno="Área Urbana", cor_hex="#ba3acb", cor_rgb="(186,58,203)")
    add_entorno(variavel_entorno="Solo Exposto", cor_hex="#d49c00", cor_rgb="(212,156,0)")
    add_entorno(variavel_entorno="Uso do Solo", cor_hex="#74a048", cor_rgb="(116, 160,72)")
    add_entorno(variavel_entorno="Vegetação Secundária", cor_hex="#74fb48", cor_rgb="(116,251,72)")
    add_entorno(variavel_entorno="Água Doce", cor_hex="#0055ff", cor_rgb="(0,85,255)")
    add_entorno(variavel_entorno="Água Salobra", cor_hex="#00ffff", cor_rgb="(0,255,255)")
    add_entorno(variavel_entorno="Mar", cor_hex="#afcaff", cor_rgb="(175,202,255)")
    add_entorno(variavel_entorno="Montanha de Pedra", cor_hex="#AA5500", cor_rgb="(170,85,0)")

def add_entorno(variavel_entorno, cor_hex, cor_rgb):
    m = rbcapp.models.Entorno.objects.get_or_create(variavel_entorno=variavel_entorno, cor_hex=cor_hex, cor_rgb=cor_rgb)[0]
    m.variavel_entorno = variavel_entorno
    m.cor_hex = cor_hex
    m.cor_rgb = cor_rgb

    m.save()
    return m

# Start execution here!
if __name__ == '__main__':
    print("Starting entornos population script...")
    populate()
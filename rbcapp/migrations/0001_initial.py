# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bacia_Hidrografica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Casos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classificacao_iap', models.CharField(max_length=45)),
                ('classificacao_iva', models.CharField(max_length=45)),
                ('risco', models.CharField(max_length=1)),
                ('solucao_sugerida', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_coleta', models.DateField(verbose_name=b'Data da Coleta')),
            ],
        ),
        migrations.CreateModel(
            name='Coleta_Substancia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor_coletado', models.FloatField()),
                ('coleta', models.ForeignKey(to='rbcapp.Coleta')),
            ],
        ),
        migrations.CreateModel(
            name='Entorno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('variavel_entorno', models.CharField(max_length=45)),
                ('cor', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=150)),
                ('data_emissao', models.DateField()),
                ('imagem', models.ImageField(upload_to=b'imagem/')),
                ('coleta', models.ForeignKey(blank=True, to='rbcapp.Coleta', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Monitoramento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_monitoramento', models.DateField(verbose_name=b'Data do Monitoramento')),
                ('classificacao_iap', models.CharField(max_length=45, null=True)),
                ('classificacao_iva', models.CharField(max_length=45, null=True)),
                ('risco', models.CharField(max_length=1, null=True)),
                ('solucao_sugerida', models.TextField(null=True)),
                ('coleta', models.ForeignKey(to='rbcapp.Coleta')),
                ('entorno', models.ForeignKey(blank=True, to='rbcapp.Entorno', null=True)),
                ('imagem', models.ForeignKey(blank=True, to='rbcapp.Imagem', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ponto_Monitoramento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('dimensao', models.FloatField()),
                ('bacia_hidrografica', models.ForeignKey(to='rbcapp.Bacia_Hidrografica')),
            ],
        ),
        migrations.CreateModel(
            name='Substancia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=11)),
                ('pergunta', models.CharField(max_length=20)),
                ('resposta', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='ponto_monitoramento',
            name='rio',
            field=models.ForeignKey(to='rbcapp.Rio'),
        ),
        migrations.AddField(
            model_name='monitoramento',
            name='ponto_monitoramento',
            field=models.ForeignKey(to='rbcapp.Ponto_Monitoramento'),
        ),
        migrations.AddField(
            model_name='imagem',
            name='ponto_monitoramento',
            field=models.ForeignKey(to='rbcapp.Ponto_Monitoramento'),
        ),
        migrations.AddField(
            model_name='coleta_substancia',
            name='substancia',
            field=models.ForeignKey(to='rbcapp.Substancia'),
        ),
        migrations.AddField(
            model_name='coleta',
            name='ponto_monitoramento',
            field=models.ForeignKey(to='rbcapp.Ponto_Monitoramento'),
        ),
        migrations.AddField(
            model_name='coleta',
            name='substancia',
            field=models.ManyToManyField(to='rbcapp.Substancia', through='rbcapp.Coleta_Substancia'),
        ),
        migrations.AddField(
            model_name='casos',
            name='entorno',
            field=models.ForeignKey(to='rbcapp.Entorno'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil', '0004_auto_20150112_1603'),
        ('Docentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_empresa', models.CharField(max_length=250, null=True, blank=True)),
                ('giro', models.CharField(max_length=250, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_poryecto', models.CharField(max_length=250, null=True, blank=True)),
                ('opcion_elegida', models.CharField(max_length=50, null=True, blank=True)),
                ('asesor_interno', models.ForeignKey(blank=True, to='Docentes.Asesor_Interno', null=True)),
                ('carrera', models.ForeignKey(blank=True, to='Perfil.Carrera', null=True)),
                ('empresa', models.OneToOneField(null=True, blank=True, to='Residencia.Empresa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

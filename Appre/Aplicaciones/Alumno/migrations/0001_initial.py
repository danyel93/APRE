# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calle', models.CharField(max_length=250, null=True, blank=True)),
                ('numero_casa', models.CharField(max_length=10, null=True, blank=True)),
                ('colonia', models.CharField(max_length=100, null=True, blank=True)),
                ('tipo_seguro', models.CharField(max_length=50, null=True, blank=True)),
                ('num_seguro', models.CharField(max_length=20, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=100, null=True, blank=True)),
                ('tel_casa', models.CharField(max_length=20, null=True, blank=True)),
                ('cali_ai', models.PositiveSmallIntegerField(max_length=3, null=True, blank=True)),
                ('cali_ae', models.PositiveSmallIntegerField(max_length=3, null=True, blank=True)),
                ('cali_final', models.PositiveSmallIntegerField(max_length=3, null=True, blank=True)),
                ('intentos', models.TextField()),
                ('carrera', models.ForeignKey(blank=True, to='Perfil.Carrera', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cronograma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objetivos_especificos', models.TextField()),
                ('etapa_1', models.CharField(max_length=100, null=True, blank=True)),
                ('etapa_2', models.CharField(max_length=100, null=True, blank=True)),
                ('etapa_3', models.CharField(max_length=100, null=True, blank=True)),
                ('c1_ai', models.BooleanField(default=False)),
                ('c2_ai', models.BooleanField(default=False)),
                ('c3_ai', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='alumno',
            name='cronograma',
            field=models.OneToOneField(null=True, blank=True, to='Alumno.Cronograma'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alumno',
            name='perfil',
            field=models.OneToOneField(null=True, blank=True, to='Perfil.Perfil'),
            preserve_default=True,
        ),
    ]

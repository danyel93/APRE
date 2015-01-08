# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_estudios', models.CharField(max_length=100, null=True, blank=True)),
                ('nombre_carrera', models.CharField(max_length=100, null=True, blank=True)),
                ('modalidad', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
                ('llave', models.CharField(max_length=100)),
                ('fecha_creada', models.DateField(default=django.utils.timezone.now)),
                ('fecha_caducidad', models.DateField(default=datetime.datetime(2015, 1, 15, 16, 6, 28, 855000))),
                ('validada', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_p', models.CharField(max_length=50)),
                ('apellido_m', models.CharField(max_length=50)),
                ('numero_control', models.CharField(max_length=150)),
                ('tel_movil', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to=b'Imagenes/avatares/%Y/%m/%d')),
                ('fecha_registro', models.DateField(default=django.utils.timezone.now)),
                ('tipo_usuario', models.CharField(max_length=50, null=True, blank=True)),
                ('editar', models.BooleanField(default=True)),
                ('activo', models.BooleanField(default=False)),
                ('codigo', models.OneToOneField(null=True, blank=True, to='Perfil.Codigo')),
                ('usuario', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

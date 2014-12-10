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
            name='Codigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
                ('llave', models.CharField(max_length=100)),
                ('fecha_creada', models.DateField(default=django.utils.timezone.now)),
                ('fecha_caducidad', models.DateField(default=datetime.datetime(2014, 12, 16, 20, 46, 24, 820000))),
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
                ('fecha_registro', models.DateField(default=django.utils.timezone.now)),
                ('numero_control', models.CharField(max_length=150)),
                ('celular', models.CharField(max_length=50)),
                ('verificacion', models.BooleanField(default=False)),
                ('tipo_usuario', models.CharField(max_length=50, null=True, blank=True)),
                ('editar', models.BooleanField(default=True)),
                ('usuario', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='codigo',
            name='perfil',
            field=models.ForeignKey(blank=True, to='Perfil.Perfil', null=True),
            preserve_default=True,
        ),
    ]

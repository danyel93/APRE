# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_p', models.CharField(max_length=50)),
                ('apellido_m', models.CharField(max_length=50)),
                ('fecha_registro', models.DateField(default=django.utils.timezone.now)),
                ('numero_control', models.CharField(max_length=150)),
                ('celuar', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

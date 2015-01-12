# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil', '0004_auto_20150112_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesor_Interno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento', models.CharField(max_length=100)),
                ('perfil', models.ForeignKey(blank=True, to='Perfil.Perfil', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

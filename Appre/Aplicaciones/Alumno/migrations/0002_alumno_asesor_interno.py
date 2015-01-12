# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Docentes', '0001_initial'),
        ('Alumno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='asesor_interno',
            field=models.ForeignKey(blank=True, to='Docentes.Asesor_Interno', null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigo',
            name='fecha_caducidad',
            field=models.DateField(default=datetime.datetime(2015, 1, 15, 16, 7, 59, 287000)),
            preserve_default=True,
        ),
    ]

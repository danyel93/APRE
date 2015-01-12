# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil', '0004_auto_20150112_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigo',
            name='fecha_caducidad',
            field=models.DateField(default=datetime.datetime(2015, 1, 19, 16, 9, 6, 350000)),
            preserve_default=True,
        ),
    ]

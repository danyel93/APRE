# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil', '0003_auto_20150108_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigo',
            name='fecha_caducidad',
            field=models.DateField(default=datetime.datetime(2015, 1, 19, 16, 3, 18, 490000)),
            preserve_default=True,
        ),
    ]

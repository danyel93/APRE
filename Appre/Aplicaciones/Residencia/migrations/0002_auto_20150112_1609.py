# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Residencia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='nombre_poryecto',
            new_name='nombre_proyecto',
        ),
    ]

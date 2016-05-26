# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appTpv', '0005_auto_20160317_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='camarero',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appTpv', '0004_auto_20160317_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

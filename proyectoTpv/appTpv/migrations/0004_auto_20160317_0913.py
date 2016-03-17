# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appTpv', '0003_auto_20160316_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='fecha_fin',
            field=models.DateTimeField(null=True),
        ),
    ]

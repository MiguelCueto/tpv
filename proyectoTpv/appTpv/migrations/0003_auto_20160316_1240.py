# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appTpv', '0002_saldo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='articulo',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='factura',
            name='abierto',
            field=models.NullBooleanField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appTpv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('fecha_saldo', models.DateTimeField()),
                ('saldo_actual', models.FloatField()),
            ],
        ),
    ]

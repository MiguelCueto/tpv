# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articulo', models.CharField(max_length=100)),
                ('precio_unitario', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Camarero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Cantidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('articulo', models.ForeignKey(to='appTpv.Articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('camarero', models.ForeignKey(to='appTpv.Camarero')),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('camarero', models.ForeignKey(to='appTpv.Camarero')),
            ],
        ),
        migrations.AddField(
            model_name='cantidad',
            name='factura',
            field=models.ForeignKey(to='appTpv.Factura'),
        ),
        migrations.AlterUniqueTogether(
            name='periodo',
            unique_together=set([('fecha_inicio', 'camarero')]),
        ),
    ]

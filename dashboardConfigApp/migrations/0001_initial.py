# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('descripcion', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Capa_Indicador',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('valor', models.CharField(max_length=100)),
                ('capa', models.ForeignKey(to='dashboardConfigApp.Capa')),
            ],
        ),
        migrations.CreateModel(
            name='Condicion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Condicion_Capa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('color', models.CharField(max_length=11)),
                ('capa', models.ForeignKey(to='dashboardConfigApp.Capa')),
                ('codicion', models.ForeignKey(to='dashboardConfigApp.Condicion')),
            ],
        ),
        migrations.CreateModel(
            name='Condicion_Indicador',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('valorComparar', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=11)),
                ('codicion', models.ForeignKey(to='dashboardConfigApp.Condicion')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.FileField(upload_to='images/', default='images/none_image.jpg')),
            ],
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fechaCreacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCampo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('descripcion', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='indicador',
            name='tipo',
            field=models.ForeignKey(to='dashboardConfigApp.TipoCampo'),
        ),
        migrations.AddField(
            model_name='image',
            name='proyecto',
            field=models.ForeignKey(to='dashboardConfigApp.Proyecto'),
        ),
        migrations.AddField(
            model_name='condicion_indicador',
            name='indicador',
            field=models.ForeignKey(to='dashboardConfigApp.Indicador'),
        ),
        migrations.AddField(
            model_name='capa_indicador',
            name='indicador',
            field=models.ForeignKey(to='dashboardConfigApp.Indicador'),
        ),
        migrations.AddField(
            model_name='capa',
            name='image',
            field=models.ForeignKey(to='dashboardConfigApp.Image'),
        ),
    ]

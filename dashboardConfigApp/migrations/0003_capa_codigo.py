# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardConfigApp', '0002_proyecto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='capa',
            name='codigo',
            field=models.CharField(max_length=50, default=''),
        ),
    ]

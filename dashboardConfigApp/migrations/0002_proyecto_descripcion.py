# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardConfigApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='descripcion',
            field=models.CharField(max_length=100, default=''),
        ),
    ]

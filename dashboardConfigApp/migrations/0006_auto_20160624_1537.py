# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardConfigApp', '0005_remove_indicador_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='capa_indicador',
            name='proyecto',
            field=models.ForeignKey(default=None, to='dashboardConfigApp.Proyecto'),
        ),
        migrations.AddField(
            model_name='indicador',
            name='proyecto',
            field=models.ForeignKey(default=None, to='dashboardConfigApp.Proyecto'),
        ),
    ]

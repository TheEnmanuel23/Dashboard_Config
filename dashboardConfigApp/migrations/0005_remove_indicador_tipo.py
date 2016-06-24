# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardConfigApp', '0004_auto_20160615_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicador',
            name='tipo',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardConfigApp', '0003_capa_codigo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capa',
            old_name='codigo',
            new_name='idCapa',
        ),
    ]

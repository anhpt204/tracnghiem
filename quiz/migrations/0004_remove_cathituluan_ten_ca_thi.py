# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20150909_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cathituluan',
            name='ten_ca_thi',
        ),
    ]

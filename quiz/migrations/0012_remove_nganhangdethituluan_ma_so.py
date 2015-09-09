# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20150909_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nganhangdethituluan',
            name='ma_so',
        ),
    ]

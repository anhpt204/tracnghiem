# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20150907_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dethituluan',
            old_name='file_path',
            new_name='de_thi',
        ),
    ]

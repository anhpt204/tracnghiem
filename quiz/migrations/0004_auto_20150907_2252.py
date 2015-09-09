# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20150907_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lop',
            name='doi_tuong',
            field=models.ForeignKey(default=1, verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng', to='quiz.DoiTuong'),
            preserve_default=False,
        ),
    ]

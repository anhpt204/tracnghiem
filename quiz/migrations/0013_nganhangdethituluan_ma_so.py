# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_remove_nganhangdethituluan_ma_so'),
    ]

    operations = [
        migrations.AddField(
            model_name='nganhangdethituluan',
            name='ma_so',
            field=models.CharField(max_length=20, null=True, verbose_name=b'M\xc3\xa3 b\xe1\xbb\x99 \xc4\x91\xe1\xbb\x81', blank=True),
        ),
    ]

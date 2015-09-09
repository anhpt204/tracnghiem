# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20150909_2227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dethituluan',
            options={'verbose_name': '\u0110\u1ec1 thi t\u1ef1 lu\u1eadn', 'verbose_name_plural': 'Danh s\xe1ch \u0111\u1ec1 thi t\u1ef1 lu\u1eadn'},
        ),
        migrations.AddField(
            model_name='nganhangdethituluan',
            name='ma_so',
            field=models.CharField(default=1, unique=True, max_length=20, verbose_name=b'M\xc3\xa3 b\xe1\xbb\x99 \xc4\x91\xe1\xbb\x81'),
            preserve_default=False,
        ),
    ]

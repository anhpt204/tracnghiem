# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_cathituluan_ten_ca_thi'),
    ]

    operations = [
        migrations.AddField(
            model_name='cathituluan',
            name='ten_ca_thi',
            field=models.CharField(default=1, max_length=100, verbose_name=b'Ti\xc3\xaau \xc4\x91\xe1\xbb\x81 ca thi'),
            preserve_default=False,
        ),
    ]

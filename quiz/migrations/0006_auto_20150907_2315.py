# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20150907_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nganhangdethituluan',
            name='ngay_tao',
            field=models.DateField(default=datetime.datetime(2015, 9, 7, 23, 15, 25, 116160), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o'),
        ),
    ]

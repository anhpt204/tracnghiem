# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20150907_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nganhangdethituluan',
            name='ngay_tao',
            field=models.DateField(default=datetime.date(2015, 9, 7), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o'),
        ),
    ]

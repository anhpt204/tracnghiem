# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20150907_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='NganHangDeThiTuLuan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ngay_tao', models.DateTimeField(default=datetime.datetime(2015, 9, 7, 23, 8, 39, 338077), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o')),
                ('doi_tuong', models.ForeignKey(verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng thi', to='quiz.DoiTuong')),
                ('mon_thi', models.ForeignKey(verbose_name=b'M\xc3\xb4n thi', to='quiz.MonThi')),
            ],
        ),
        migrations.RemoveField(
            model_name='dethituluan',
            name='doi_tuong',
        ),
        migrations.RemoveField(
            model_name='dethituluan',
            name='mon_thi',
        ),
        migrations.RemoveField(
            model_name='dethituluan',
            name='ngay_tao',
        ),
        migrations.AddField(
            model_name='dethituluan',
            name='ma_de_thi',
            field=models.CharField(default=1, unique=True, max_length=10, verbose_name=b'M\xc3\xa3 \xc4\x91\xe1\xbb\x81 thi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dethituluan',
            name='ngan_hang',
            field=models.ForeignKey(default=1, verbose_name=b'Ng\xc3\xa2n h\xc3\xa0ng', to='quiz.NganHangDeThiTuLuan'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20150907_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaThiTuLuan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ngay_thi', models.DateField(verbose_name=b'Ng\xc3\xa0y thi')),
                ('so_de_thi', models.PositiveIntegerField(default=1, help_text=b'S\xe1\xbb\x91 \xc4\x91\xe1\xbb\x81 thi l\xc3\xa0 s\xe1\xbb\x91 nguy\xc3\xaan d\xc6\xb0\xc6\xa1ng, l\xe1\xbb\x9bn h\xc6\xa1n 0', verbose_name=b'S\xe1\xbb\x91 \xc4\x91\xe1\xbb\x81 thi')),
                ('doi_tuong', models.ForeignKey(verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng', to='quiz.DoiTuong')),
                ('ds_de_thi', models.ManyToManyField(to='quiz.DeThiTuLuan', null=True, blank=True)),
                ('giam_thi', models.ManyToManyField(to='quiz.GiaoVien', verbose_name=b'Gi\xc3\xa1m th\xe1\xbb\x8b')),
                ('lop', models.ForeignKey(verbose_name=b'L\xe1\xbb\x9bp', to='quiz.Lop')),
                ('mon_thi', models.ForeignKey(verbose_name=b'M\xc3\xb4n thi', to='quiz.MonThi')),
            ],
        ),
        migrations.AlterModelOptions(
            name='nganhangdethituluan',
            options={'verbose_name': 'Ng\xe2n h\xe0ng \u0111\u1ec1 thi t\u1ef1 lu\u1eadn'},
        ),
        migrations.AlterField(
            model_name='nganhangdethituluan',
            name='ngay_tao',
            field=models.DateField(default=datetime.date(2015, 9, 9), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o'),
        ),
    ]

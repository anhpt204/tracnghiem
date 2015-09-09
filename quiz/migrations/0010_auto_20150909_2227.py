# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20150909_0006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cathituluan',
            options={'verbose_name': 'Ca thi t\u1ef1 lu\u1eadn', 'verbose_name_plural': 'Danh s\xe1ch ca thi t\u1ef1 lu\u1eadn'},
        ),
        migrations.AlterModelOptions(
            name='nganhangdethituluan',
            options={'verbose_name': 'B\u1ed9 \u0111\u1ec1 thi t\u1ef1 lu\u1eadn'},
        ),
        migrations.AddField(
            model_name='cathituluan',
            name='hoc_ky',
            field=models.CharField(default=b'HK1', max_length=3, verbose_name=b'H\xe1\xbb\x8dc k\xe1\xbb\xb3', choices=[(b'HK1', b'H\xe1\xbb\x8dc k\xe1\xbb\xb3 1'), (b'HK2', b'H\xe1\xbb\x8dc k\xe1\xbb\xb3 2')]),
        ),
        migrations.AddField(
            model_name='cathituluan',
            name='nam_hoc',
            field=models.CharField(default=-1, help_text=b'Nh\xe1\xba\xadp n\xc4\x83m h\xe1\xbb\x8dc theo \xc4\x91\xe1\xbb\x8bnh d\xe1\xba\xa1ng XXXX-XXXX. V\xc3\xad d\xe1\xbb\xa5 2015-2016', max_length=9, verbose_name=b'N\xc4\x83m h\xe1\xbb\x8dc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cathituluan',
            name='ten_ca_thi',
            field=models.CharField(default=1, max_length=100, verbose_name=b'Ti\xc3\xaau \xc4\x91\xe1\xbb\x81 ca thi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dethituluan',
            name='dap_an',
            field=models.FileField(upload_to=b'uploads/essay/%Y/%m/%d', null=True, verbose_name=b'\xc4\x90\xc3\xa1p \xc3\xa1n', blank=True),
        ),
        migrations.AlterField(
            model_name='cathituluan',
            name='ds_de_thi',
            field=models.ManyToManyField(to='quiz.DeThiTuLuan', verbose_name='DT', blank=True),
        ),
        migrations.AlterField(
            model_name='cathituluan',
            name='giam_thi',
            field=models.ManyToManyField(to='quiz.GiaoVien', verbose_name='Danh s\xe1ch gi\xe1m th\u1ecb coi thi'),
        ),
        migrations.AlterField(
            model_name='cathituluan',
            name='so_de_thi',
            field=models.PositiveIntegerField(default=1, help_text='S\u1ed1 \u0111\u1ec1 thi l\xe0 s\u1ed1 nguy\xean d\u01b0\u01a1ng, l\u1edbn h\u01a1n 0', verbose_name=b'S\xe1\xbb\x91 \xc4\x91\xe1\xbb\x81 thi'),
        ),
        migrations.AlterField(
            model_name='dethituluan',
            name='ma_de_thi',
            field=models.CharField(max_length=10, verbose_name=b'M\xc3\xa3 \xc4\x91\xe1\xbb\x81 thi'),
        ),
        migrations.AlterField(
            model_name='nganhangdethituluan',
            name='ngay_tao',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o'),
        ),
    ]

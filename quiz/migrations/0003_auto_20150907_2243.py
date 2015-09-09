# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0002_auto_20150615_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter_Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter', models.PositiveIntegerField(default=1, help_text=b'v\xc3\xad d\xe1\xbb\xa5: 1,2,...', verbose_name=b'Ch\xc6\xb0\xc6\xa1ng')),
                ('num_of_questions', models.PositiveIntegerField(default=1, verbose_name=b's\xe1\xbb\x91 c\xc3\xa2u h\xe1\xbb\x8fi')),
            ],
            options={
                'verbose_name': 'Thi\u1ebft l\u1eadp s\u1ed1 c\xe2u h\u1ecfi cho t\u1eebng ch\u01b0\u01a1ng',
                'verbose_name_plural': 'Thi\u1ebft l\u1eadp s\u1ed1 c\xe2u h\u1ecfi cho t\u1eebng ch\u01b0\u01a1ng',
            },
        ),
        migrations.CreateModel(
            name='DeThiTuLuan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_path', models.FileField(upload_to=b'uploads/essay/%Y/%m/%d', null=True, verbose_name=b'\xc4\x90\xe1\xbb\x81 thi', blank=True)),
                ('ngay_tao', models.DateTimeField(verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o')),
            ],
        ),
        migrations.CreateModel(
            name='DoiTuong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_dt', models.CharField(help_text=b'M\xc3\xa3 kh\xc3\xb4ng qu\xc3\xa1 10 k\xc3\xbd t\xe1\xbb\xb1', unique=True, max_length=10, verbose_name=b'M\xc3\xa3 \xc4\x91\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng')),
                ('ten_dt', models.CharField(unique=True, max_length=50, verbose_name=b'T\xc3\xaan \xc4\x91\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng')),
            ],
            options={
                'verbose_name': '\u0110\u1ed1i t\u01b0\u1ee3ng',
                'verbose_name_plural': 'Danh s\xe1ch \u0111\u1ed1i t\u01b0\u1ee3ng',
            },
        ),
        migrations.CreateModel(
            name='DonVi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_dv', models.CharField(help_text=b'M\xc3\xa3 \xc4\x91\xc6\xa1n v\xe1\xbb\x8b kh\xc3\xb4ng qu\xc3\xa1 5 k\xc3\xbd t\xe1\xbb\xb1', unique=True, max_length=5, verbose_name=b'M\xc3\xa3 \xc4\x91\xc6\xa1n v\xe1\xbb\x8b')),
                ('ten_dv', models.CharField(unique=True, max_length=200, verbose_name=b'T\xc3\xaan \xc4\x91\xc6\xa1n v\xe1\xbb\x8b')),
                ('cha_dv', models.ForeignKey(blank=True, to='quiz.DonVi', help_text=b'\xc4\x90\xc6\xa1n v\xe1\xbb\x8b c\xe1\xba\xa5p tr\xc3\xaan tr\xe1\xbb\xb1c ti\xe1\xba\xbfp', null=True, verbose_name=b'\xc4\x90\xc6\xa1n v\xe1\xbb\x8b c\xe1\xba\xa5p tr\xc3\xaan')),
            ],
            options={
                'verbose_name': '\u0110\u01a1n v\u1ecb',
                'verbose_name_plural': 'Danh s\xe1ch \u0111\u01a1n v\u1ecb',
            },
        ),
        migrations.CreateModel(
            name='GiaoVien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_so', models.PositiveIntegerField(unique=True, verbose_name=b'M\xc3\xa3 s\xe1\xbb\x91')),
                ('ho_ten', models.CharField(max_length=50, verbose_name=b'H\xe1\xbb\x8d v\xc3\xa0 t\xc3\xaan')),
                ('don_vi', models.ForeignKey(verbose_name=b'\xc4\x90\xc6\xa1n v\xe1\xbb\x8b', to='quiz.DonVi', help_text=b'\xc4\x90\xc6\xa1n v\xe1\xbb\x8b qu\xe1\xba\xa3n l\xc3\xbd tr\xe1\xbb\xb1c ti\xe1\xba\xbfp')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gi\xe1o vi\xean',
                'verbose_name_plural': 'Danh s\xe1ch gi\xe1o vi\xean',
            },
        ),
        migrations.CreateModel(
            name='Lop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_lop', models.CharField(unique=True, max_length=5, verbose_name=b'M\xc3\xa3 l\xe1\xbb\x9bp')),
                ('ten_lop', models.CharField(unique=True, max_length=200, verbose_name=b'L\xe1\xbb\x9bp')),
                ('si_so', models.PositiveIntegerField(null=True, verbose_name=b'S\xc4\xa9 s\xe1\xbb\x91', blank=True)),
                ('doi_tuong', models.ForeignKey(default=1, blank=True, to='quiz.DoiTuong', null=True, verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng')),
            ],
            options={
                'verbose_name': 'L\u1edbp',
                'verbose_name_plural': 'Danh s\xe1ch l\u1edbp',
            },
        ),
        migrations.CreateModel(
            name='Lop_CaThi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionGroup_Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_type', models.CharField(default=b'MC', max_length=5, verbose_name=b'Lo\xe1\xba\xa1i c\xc3\xa2u h\xe1\xbb\x8fi', choices=[(b'TF', b'C\xc3\xa2u h\xe1\xbb\x8fi \xc4\x90\xc3\xbang - Sai'), (b'MC', b'C\xc3\xa2u h\xe1\xbb\x8fi Multiple Choice'), (b'ESSAY', b'C\xc3\xa2u h\xe1\xbb\x8fi t\xe1\xbb\xb1 lu\xe1\xba\xadn')])),
                ('mark_per_question', models.PositiveIntegerField(default=1, verbose_name=b'\xc4\x90i\xe1\xbb\x83m cho m\xe1\xbb\x97i c\xc3\xa2u h\xe1\xbb\x8fi')),
                ('num_of_questions', models.PositiveIntegerField(default=1, verbose_name=b's\xe1\xbb\x91 c\xc3\xa2u h\xe1\xbb\x8fi')),
            ],
            options={
                'verbose_name': 'C\u1ea5u h\xecnh ca thi',
                'verbose_name_plural': 'C\u1ea5u h\xecnh ca thi',
            },
        ),
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_sv', models.PositiveIntegerField(unique=True, verbose_name=b'M\xc3\xa3 sinh vi\xc3\xaan')),
                ('ho_ten', models.CharField(max_length=50, verbose_name=b'H\xe1\xbb\x8d v\xc3\xa0 t\xc3\xaan')),
                ('lop', models.ForeignKey(verbose_name=b'L\xe1\xbb\x9bp', to='quiz.Lop')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sinh vi\xean',
                'verbose_name_plural': 'Danh s\xe1ch sinh vi\xean',
            },
        ),
        migrations.RenameModel(
            old_name='DMMonThi',
            new_name='MonThi',
        ),
        migrations.RemoveField(
            model_name='cathi_setting',
            name='ca_thi',
        ),
        migrations.RemoveField(
            model_name='cathi_setting',
            name='question_group',
        ),
        migrations.RemoveField(
            model_name='dmsinhvien',
            name='lop',
        ),
        migrations.RemoveField(
            model_name='dmsinhvien',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cathi',
            name='lop_thi',
        ),
        migrations.AddField(
            model_name='diem',
            name='trang_thai_thi',
            field=models.CharField(default=b'DA_THI', max_length=20, verbose_name=b'Tr\xe1\xba\xa1ng th\xc3\xa1i thi', choices=[(b'DA_THI', b'\xc4\x90\xc3\xa3 thi'), (b'VANG_CO_LD', b'V\xe1\xba\xafng c\xc3\xb3 l\xc3\xbd do'), (b'VANG_KO_LD', b'V\xe1\xba\xafng kh\xc3\xb4ng l\xc3\xbd do')]),
        ),
        migrations.AddField(
            model_name='question',
            name='chapter',
            field=models.PositiveIntegerField(default=1, verbose_name=b'Ch\xc6\xb0\xc6\xa1ng'),
        ),
        migrations.AlterField(
            model_name='dethi',
            name='sinh_vien',
            field=models.ForeignKey(verbose_name=b'Sinh Vi\xc3\xaan', to='quiz.SinhVien'),
        ),
        migrations.AlterField(
            model_name='diem',
            name='diem',
            field=models.CommaSeparatedIntegerField(max_length=5, null=True, verbose_name=b'\xc4\x90i\xe1\xbb\x83m', blank=True),
        ),
        migrations.AlterField(
            model_name='diem',
            name='sinh_vien',
            field=models.ForeignKey(verbose_name=b'Sinh vi\xc3\xaan', to='quiz.SinhVien'),
        ),
        migrations.AlterUniqueTogether(
            name='diem',
            unique_together=set([('sinh_vien', 'mon_thi')]),
        ),
        migrations.DeleteModel(
            name='CaThi_Setting',
        ),
        migrations.DeleteModel(
            name='DMLop',
        ),
        migrations.DeleteModel(
            name='DMSinhVien',
        ),
        migrations.AddField(
            model_name='questiongroup_setting',
            name='ca_thi',
            field=models.ForeignKey(verbose_name=b'Ca thi', to='quiz.CaThi'),
        ),
        migrations.AddField(
            model_name='questiongroup_setting',
            name='question_group',
            field=models.ForeignKey(verbose_name=b'Nh\xc3\xb3m c\xc3\xa2u h\xe1\xbb\x8fi', to='quiz.QuestionGroup'),
        ),
        migrations.AddField(
            model_name='lop_cathi',
            name='ds_sinhvien',
            field=models.ManyToManyField(to='quiz.SinhVien'),
        ),
        migrations.AddField(
            model_name='lop_cathi',
            name='lop',
            field=models.ForeignKey(verbose_name=b'L\xe1\xbb\x9bp thi', to='quiz.Lop'),
        ),
        migrations.AddField(
            model_name='dethituluan',
            name='doi_tuong',
            field=models.ForeignKey(verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng thi', to='quiz.DoiTuong'),
        ),
        migrations.AddField(
            model_name='dethituluan',
            name='mon_thi',
            field=models.ForeignKey(verbose_name=b'M\xc3\xb4n thi', to='quiz.MonThi'),
        ),
        migrations.AddField(
            model_name='chapter_setting',
            name='ca_thi',
            field=models.ForeignKey(verbose_name=b'Ca thi', to='quiz.CaThi'),
        ),
        migrations.AddField(
            model_name='cathi',
            name='ds_giamthi',
            field=models.ManyToManyField(to='quiz.GiaoVien', verbose_name='Danh s\xe1ch gi\xe1m th\u1ecb coi thi'),
        ),
        migrations.AddField(
            model_name='cathi',
            name='ds_thisinh',
            field=models.ManyToManyField(help_text=b'T\xc3\xacm ki\xe1\xba\xbfm theo h\xe1\xbb\x8d t\xc3\xaan sinh vi\xc3\xaan ho\xe1\xba\xb7c m\xc3\xa3 l\xe1\xbb\x9bp.', to='quiz.SinhVien', verbose_name='Danh s\xe1ch th\xed sinh'),
        ),
    ]

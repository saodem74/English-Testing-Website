# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testEng', '0005_auto_20160514_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word_cate',
            name='id_user',
        ),
        migrations.AddField(
            model_name='word_cate',
            name='id_word',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testEng.word'),
        ),
    ]

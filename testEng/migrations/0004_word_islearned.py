# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testEng', '0003_remove_word_id_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='isLearned',
            field=models.BooleanField(default=False),
        ),
    ]

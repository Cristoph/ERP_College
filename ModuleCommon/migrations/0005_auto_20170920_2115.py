# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleCommon', '0004_auto_20170920_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='ModuleCommon.Teacher'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleCommon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

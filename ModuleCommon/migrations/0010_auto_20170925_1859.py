# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleCommon', '0009_qualification_periodo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rode', models.IntegerField()),
                ('tariff', models.IntegerField()),
                ('monthly', models.IntegerField()),
                ('total', models.IntegerField()),
                ('remaining', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('period', models.IntegerField()),
                ('grade', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ModuleCommon.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RenameField(
            model_name='qualification',
            old_name='periodo',
            new_name='period',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='attorney',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='attorney',
            name='cellphone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='attorney',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='cellphone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='cellphone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='teacher_subject',
            name='subject',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ModuleCommon.Subject'),
        ),
        migrations.AddField(
            model_name='teacher_subject',
            name='teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ModuleCommon.Teacher'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ModuleCommon.Student'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='teacher_subject',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='ModuleCommon.Teacher_Subject'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20170509_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='first_level',
            field=models.ManyToManyField(blank=True, to='variables.Level_Expertise'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='second_level',
            field=models.ManyToManyField(blank=True, related_name='level2', to='variables.Level_Expertise'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='third_level',
            field=models.ManyToManyField(blank=True, related_name='level3', to='variables.Level_Expertise'),
        ),
    ]
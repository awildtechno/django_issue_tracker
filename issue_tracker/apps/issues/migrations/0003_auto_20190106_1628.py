# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-07 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20190101_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resolvedissue',
            name='created_on',
            field=models.DateField(),
        ),
    ]
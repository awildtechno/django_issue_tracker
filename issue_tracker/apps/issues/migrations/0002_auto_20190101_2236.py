# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-02 06:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resolvedissue',
            name='old_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resolvedissue',
            name='resolved_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resolvedissue',
            name='serialized_log',
            field=models.TextField(null=True),
        ),
    ]
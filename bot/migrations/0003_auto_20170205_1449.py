# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_bot_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='botplugin',
            name='context',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='botplugin',
            name='type',
            field=models.CharField(choices=[('py1', 'python_simple_plugin_ver1')], default='py1', max_length=255),
            preserve_default=False,
        ),
    ]

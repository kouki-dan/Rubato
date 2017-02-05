# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 03:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('provider', models.CharField(choices=[('s', 'slack')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='BotPlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('required_parameters', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.TextField()),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.Bot')),
                ('bot_plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.BotPlugin')),
            ],
        ),
        migrations.AddField(
            model_name='bot',
            name='plugins',
            field=models.ManyToManyField(through='bot.Plugin', to='bot.BotPlugin'),
        ),
        migrations.AddField(
            model_name='bot',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

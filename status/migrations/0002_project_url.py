# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.SlugField(default='test', verbose_name='URL: /ping/'),
            preserve_default=False,
        ),
    ]

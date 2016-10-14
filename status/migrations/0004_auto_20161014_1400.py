# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_auto_20161014_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='alertAfter_s',
            field=models.IntegerField(default=60, help_text='It is reccomended that you set this slightly longer than the interval you plan on pinging. e.g. If you plan on sending a ping every 60 seconds, set this to 65.', verbose_name='Send alert after not reciving a ping for (in seconds)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='alertedContacts',
            field=models.ManyToManyField(help_text='Note: you will automatically recieve an email, no need to add your email here', to='status.Contact', verbose_name='Emails to send alerts to'),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.SlugField(help_text='The url that your application sends pings to will be /ping/[this field]', unique=True, verbose_name='URL'),
        ),
    ]

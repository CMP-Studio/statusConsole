# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 20:34
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
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Project Name')),
                ('alertAfter_s', models.IntegerField(default=60, verbose_name='Send alert after (in seconds)')),
                ('active', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Active?')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Online'), (2, 'Offline (Short)'), (3, 'Offline (Long)')], default=0, editable=False, verbose_name='Status')),
                ('notified', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, editable=False, verbose_name='Admins Notified?')),
                ('lastPing', models.DateTimeField(editable=False, null=True, verbose_name='Last ping recieved')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated On')),
                ('alertedContacts', models.ManyToManyField(to='status.Contact', verbose_name='Emails to send alerts to')),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

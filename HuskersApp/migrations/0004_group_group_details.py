# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-04 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HuskersApp', '0003_auto_20180321_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_details',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-20 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IHAM_app', '0008_auto_20180121_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='customerAddress',
            field=models.TextField(),
        ),
    ]

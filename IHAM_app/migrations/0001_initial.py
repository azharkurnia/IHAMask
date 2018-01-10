# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-08 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=140)),
                ('customerEmail', models.EmailField(max_length=140)),
                ('customerPhone', models.IntegerField()),
                ('productQuantityA', models.IntegerField()),
                ('productQuantityB', models.IntegerField()),
                ('customerAddress', models.CharField(max_length=140)),
                ('totalPrice', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
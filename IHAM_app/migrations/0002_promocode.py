# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-10 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IHAM_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='promoCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promoName', models.CharField(max_length=10)),
                ('promoAmount', models.FloatField()),
            ],
        ),
    ]

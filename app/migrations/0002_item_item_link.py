# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-22 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_link',
            field=models.SlugField(default='condom', max_length=100),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-25 10:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart_session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=100, unique=True)),
                ('session_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_description', models.TextField()),
                ('item_slug', models.SlugField(max_length=100)),
                ('item_link', models.SlugField(max_length=100)),
                ('item_price', models.IntegerField(max_length=100)),
            ],
            options={
                'verbose_name': 'items',
            },
        ),
        migrations.CreateModel(
            name='state_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_item_name', models.CharField(max_length=100)),
                ('cart_item_description', models.CharField(max_length=500)),
                ('cart_item_price', models.IntegerField(blank=True)),
                ('cart_session_id', models.CharField(max_length=100)),
                ('cart_slug', models.SlugField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
            },
        ),
    ]

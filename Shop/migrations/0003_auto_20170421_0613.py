# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_auto_20170421_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_photo',
            field=models.FileField(upload_to='products/'),
        ),
    ]

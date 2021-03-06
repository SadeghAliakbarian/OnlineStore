# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_name', models.CharField(max_length=100)),
                ('dealer_category', models.CharField(choices=[('Grocery', 'Grocery'), ('Technology', 'Grocery'), ('Home', 'Home'), ('Clothing', 'Clothing'), ('Sport', 'Sport')], max_length=100)),
                ('dealer_email', models.CharField(max_length=100)),
                ('dealer_budget', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=400)),
                ('product_photo', models.FileField(upload_to='products/')),
                ('product_price', models.FloatField(default=0.0)),
                ('product_quantity', models.IntegerField(default=0)),
                ('product_dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.Dealer')),
            ],
        ),
    ]

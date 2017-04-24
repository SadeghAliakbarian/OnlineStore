# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('Grocery','Grocery'),
    ('Technology','Technology'),
    ('Home','Home'),
    ('Clothing', 'Clothing'),
    ('Sport','Sport')
)


class Dealer(models.Model):
    dealer_name = models.CharField(max_length=100)
    dealer_category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    dealer_email = models.CharField(max_length=100)
    dealer_budget = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.dealer_name)

class Product(models.Model):
    product_dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=400)
    product_photo = models.FileField()
    product_banner = models.FileField(default='')
    product_price = models.FloatField(default=0.0)
    product_quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product_name)



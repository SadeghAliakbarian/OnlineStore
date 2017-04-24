# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from models import Product, Dealer
# Create your views here.

def index(request):
    product_list = Product.objects.all()
    context = {'products': product_list}
    return render(request, 'Shop/index.html', context)


def products(request):
    product_list = Product.objects.all()
    context = {'products':product_list}
    return render(request, 'Shop/product_list.html', context)


def dealers(request):
    dealer_list = Dealer.objects.all()
    context = {'dealers':dealer_list}
    return render(request, 'Shop/dealer_list.html', context)


def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk = dealer_id)
    context = {'dealer':dealer}
    return render(request, 'Shop/dealer_detail.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    context = {'product':product}
    return render(request, 'Shop/product_detail.html', context)


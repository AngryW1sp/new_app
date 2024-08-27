from django.shortcuts import render
from .product_dicts import products


def catalog(request):
    context = {'products': products}
    return render(request, 'goods/catalog.html', context=context)


def product(request):
    return render(request, 'goods/product.html')

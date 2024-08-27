from django.shortcuts import render

from goods.models import Products


def catalog(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'goods/catalog.html', context=context)


def product(request):
    return render(request, 'goods/product.html')

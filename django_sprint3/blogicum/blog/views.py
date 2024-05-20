
from unicodedata import category
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

POST_COUNT = 5


def index(request):
    post_list = Post.objects.all().filter(category__is_published=True,
                                          pub_date__lte=timezone.now(),
                                          is_published=True).order_by('-pub_date')[0:POST_COUNT]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, pk):
    post = get_object_or_404(Post.objects.all().filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    ).filter(pk=pk))
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    post_list = Post.objects.all().filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
        category=category)

    return render(request, "blog/category.html", {"category": category, "post_list": post_list})


from django.db import models


class Supply(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            verbose_name='Тип питания')
    slug = models.SlugField(max_length=150, unique=True,
                            blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'Supply'
        verbose_name = 'Тип питание'
        verbose_name_plural = 'Типы питания'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            verbose_name='Наименование отдела')
    slug = models.SlugField(max_length=150, unique=True,
                            blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Type_category(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            verbose_name='Наименование вида')
    slug = models.SlugField(max_length=150, unique=True,
                            blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'type'
        verbose_name = 'Категория вида'
        verbose_name_plural = 'Категории видов'

    def __str__(self):
        return self.name


class Pets(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            verbose_name='Наименование вида')
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, null=True, verbose_name='URL')
    size = models.CharField(max_length=100, verbose_name='Размер')
    description = models.TextField(unique=True, verbose_name='Описание')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    type_category = models.ForeignKey(
        to=Type_category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, verbose_name='Колличество')
    supply = models.ForeignKey(to=Supply, on_delete=models.PROTECT)

    class Meta:
        db_table = 'pets'
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self):
        return self.name


class Product_types(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            verbose_name='Вид продукции')
    slug = models.SlugField(max_length=150, unique=True,
                            blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'product_types'
        verbose_name = 'Вид продукции'
        verbose_name_plural = 'Виды продукции'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='')

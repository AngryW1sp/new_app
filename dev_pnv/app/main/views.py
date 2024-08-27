from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст'
    }
    return render(request, 'main/about.html', context)


def pay_and_deliver(request):
    context = {
        'title': 'Информация о доставке и оплате',
        'content': 'Доставка и Оплата',
        'deliver': 'Доставка осуществляется по всей территории россии в течении 12 рабочих дней с момента оплаты и сбора заказа',
        'pays': ['СБП', 'Карта', 'Наличные при получении']
    }
    return render(request, 'main/payidel.html', context)


def contacts(request):
    context = {
        'title': 'Контактная информация',
        'content': 'Контактная инворфмация',
        'contacts': ['Номер телефона офиса - 8-977-146-52-07', 'Адресс электронной почты - Aboba@ya.ru', 'Адрес офиса - г.Москва ул.Лубянка д1']
    }
    return render(request, 'main/contacts.html', context)

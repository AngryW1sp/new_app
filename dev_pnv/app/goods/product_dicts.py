products = [
    {'id': '1',
     'image': 'deps/images/goods/set of tea table and three chairs.jpg',
     'title': 'Чайный столик и три стула',
     'description': 'Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.',
     'price': 150.00},

    {'id': '2',
     'image': 'deps/images/goods/set of tea table and two chairs.jpg',
     'title': 'Чайный столик и два стула',
     'description': 'Набор из стола и двух стульев в минималистическом стиле.',
     'price': 93.00},

    {'id': '3',
     'image': 'deps/images/goods/double bed.jpg',
     'title': 'Двухспальная кровать',
     'description': 'Кровать двухспальная с надголовником и вообще очень ортопедичная.',
     'price': 670.00},

    {'id': '4',
     'image': 'deps/images/goods/kitchen table.jpg',
     'title': 'Кухонный стол с раковиной',
     'description': 'Кухонный стол для обеда с встроенной раковиной и стульями.',
     'price': 365.00},

    {'id': '5',
     'image': 'deps/images/goods/kitchen table 2.jpg',
     'title': 'Кухонный стол с встройкой',
     'description': 'Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.',
     'price': 430.00},

    {'id': '6',
     'image': 'deps/images/goods/corner sofa.jpg',
     'title': 'Угловой диван для гостинной',
     'description': 'Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!',
     'price': 610.00},

    {'id': '7',
     'image': 'deps/images/goods/bedside table.jpg',
     'title': 'Прикроватный столик',
     'description': 'Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).',
     'price': 55.00},

    {'id': '8',
     'image': 'deps/images/goods/sofa.jpg',
     'title': 'Диван обыкновенный',
     'description': 'Диван, он же софа обыкновенная, ничего примечательного для описания.',
     'price': 190.00},

    {'id': '9',
     'image': 'deps/images/goods/office chair.jpg',
     'title': 'Стул офисный',
     'description': 'Описание товара, про то какой он классный, но это стул, что тут сказать...',
     'price': 30.00},

    {'id': '10',
     'image': 'deps/images/goods/plants.jpg',
     'title': 'Растение',
     'description': 'Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.',
     'price': 10.00},

    {'id': '11',
     'image': 'deps/images/goods/flower.jpg',
     'title': 'Цветок стилизированный',
     'description': 'Дизайнерский цветок (возможно искусственный) для украшения интерьера.',
     'price': 15.00},

    {'id': '12',
     'image': 'deps/images/goods/strange table.jpg',
     'title': 'Прикроватный столик',
     'description': 'Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.',
     'price': 25.00},
]

for product in products:
    product['sell_price'] = product['price']*0.90

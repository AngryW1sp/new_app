
import requests
from telebot import TeleBot, types


bot = TeleBot(token='7236465919:AAFvRoWMgL1sQXRwWKEHV0xCIeYhsI9nkqA')
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 5344749587
text = 'Привет, Я KittyBot!'


@bot.message_handler(commands=['start',])
def wakeup(message):
    chat = message.chat
    chat_id = chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_newcat = types.KeyboardButton('/give')
    keyboard.add(button_newcat)
    bot.send_message(chat_id=chat_id, text='Thx for ON', reply_markup=keyboard)


@bot.message_handler(commands=['give',])
def send_citty(message):

    response = requests.get(URL).json()[0].get('url')
    bot.send_photo(chat_id=message.chat.id, photo=response)


@bot.message_handler(content_types=['text'])
def say_hello(message):

    chat = message.chat
    chat_id = chat.id
    text = f'Привет {message.from_user.first_name}, Я KittyBot!'
    bot.send_message(chat_id=chat_id, text=text)


bot.infinity_polling()

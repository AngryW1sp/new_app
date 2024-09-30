from http import HTTPStatus
import json
import logging
from logging.handlers import RotatingFileHandler
import os
import sys
import time
from typing import Literal

import requests
from dotenv import load_dotenv
import telebot
from telebot import TeleBot


from exceptions import (KeysError,
                        VerdictError,
                        SendError,
                        RequestError)

load_dotenv()


PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

RETRY_PERIOD = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statusess/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}


HOMEWORK_VERDICTS = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}


def check_tokens() -> Literal[True]:
    """Проверка наличая токенов."""
    flag = True
    tokens = {
        'Токен практикума': PRACTICUM_TOKEN,
        'Токен Телеграмма': TELEGRAM_TOKEN, 'Токен чата': TELEGRAM_CHAT_ID}
    for token in tokens:
        print(tokens[token])
        if not tokens[token]:
            logging.critical(
                token, '%s отсутствует!'
                'Приложение не может продолжать работу!')
            flag = False

    return flag


def send_message(bot, message) -> None:
    """Отправка сообщения."""
    chat_id = TELEGRAM_CHAT_ID
    try:
        logging.debug('Начали отправлять сообщение!')
        bot.send_message(chat_id, message)

    except telebot.apihelper.ApiTelegramException as error:
        error_message = f'Сообщение не отправлено! Причина - {error}'
        logging.error(error_message)
        raise SendError(error_message) from error
    else:
        logging.debug('Успешная отправка сообщения: %s', message)


def get_api_answer(timestamp):
    """Проверка доступа к Api."""
    params = {'from_date': timestamp}
    try:
        homework_statuses = requests.get(
            ENDPOINT, timeout=10, headers=HEADERS, params=params)
        if homework_statuses.status_code != HTTPStatus.OK:
            # Я не придумал как эту проверку переместить еще куда-то.
            # Если при проверке подскажите, буду благодарен
            logging.error('Ошибка сервера.'
                          f'{homework_statuses.status_code}')
            raise RequestError('Ошибка сервера.'
                               f'{homework_statuses.status_code}')
        return homework_statuses.json()

    except requests.exceptions.HTTPError as error:
        raise RequestError(f'HTTP Error. Причина : {error.args[0]}') from error
    except requests.exceptions.ReadTimeout as error:
        raise RequestError('Превышено ожидание подключения.') from error
    except requests.exceptions.ConnectionError as error:
        raise RequestError('Нет соединения с сервером.') from error
    except requests.exceptions.RequestException as error:
        raise RequestError(f'Ошибка: {error}') from error
    except json.JSONDecodeError as error:
        raise RequestError(f'Ошибка: {error}.') from error
    except Exception as error:
        raise RequestError(f'Неизвестная ошибка: {error}') from error


def check_response(response):
    """Проверка на наличае нужных ключей из ответа API."""
    if not isinstance(response, dict):
        raise TypeError(
            f'Не верный тип данных в ответе.'
            f'На вход поступили данные типа {type(response)}.')
    if not all(['homeworks' in response, 'current_date' in response]):
        raise KeysError('В ответе от эндпоинта отсутствуют необходимые ключи!')
    if not isinstance(response['homeworks'], list):
        raise TypeError('Не верный тип данных в списке домашних работ.')
    else:
        return True


def parse_status(homework):
    """Проверка статуса домашней работы."""

    if 'homework_name' not in homework:
        logging.debug('Пустое значение по ключу "homework_name"')
        raise KeyError('Пустое значение по ключу "homework_name"')
    if 'status' not in homework:
        logging.debug('Пустое значение по ключу "status"')
        raise KeyError('Пустое значение по ключу "status"')

    homework_name = homework['homework_name']
    homework_status = homework['status']
    if homework_status not in HOMEWORK_VERDICTS:
        logging.error(f'Неожиданный статус домашней работы {homework_name}!')
        raise VerdictError(
            f'Неожиданный статус домашней работы {homework_name}!')

    verdict = HOMEWORK_VERDICTS[homework_status]
    logging.debug(
        f'Изменился статус проверки работы "{homework_name}". {verdict}')
    return f'Изменился статус проверки работы "{homework_name}". {verdict}'


def main():
    """Основная логика работы бота."""
    if check_tokens() is True:
        errors_log = True
        bot = TeleBot(token=TELEGRAM_TOKEN)
        timestamp = 1
        while True:
            try:
                response = get_api_answer(timestamp)
                if check_response(response) is True:
                    if (len(response['homeworks']) > 0
                            and 'status' in response['homeworks'][0]):
                        homework = response['homeworks'][0]
                        send_message(bot, parse_status(homework))
                        errors_logs = True
                        timestamp = response["current_date"]
                    elif len(response['homeworks']) == 0:
                        logging.debug('Отсутствует изменение статуса')
            except Exception as error:
                message = f'Сбой в работе программы: {error}'
                logging.error(message)
                if errors_log:
                    errors_logs = False
                    send_message(bot, message)
            finally:
                time.sleep(RETRY_PERIOD)
    else:
        sys.exit('Бот не может продолжать работу!')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            RotatingFileHandler(
                'main.log', maxBytes=50000000, backupCount=5)
        ]
    )
    main()

class SendError(Exception):
    """Ошибка при отправке сообщения"""


class KeysError(Exception):
    """Ошибка наличая ключей"""


class VerdictError(Exception):
    """Ошибка статуса Домашней работы"""


class RequestError(Exception):
    """Ошибки модуля requests"""

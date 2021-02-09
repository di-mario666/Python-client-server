"""Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
    клиент отправляет запрос серверу;
    сервер отвечает соответствующим кодом результата.
    Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
Функции клиента: 
сформировать presence-сообщение; 
отправить сообщение серверу; 
получить ответ сервера; 
разобрать сообщение сервера; 
параметры командной строки скрипта client.py <addr> [<port>]: addr — ip-адрес сервера; 
port — tcp-порт на сервере, по умолчанию 7777. 
Функции сервера: 
принимает сообщение клиента; 
формирует ответ клиенту; 
отправляет ответ клиенту; 
имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777); -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)"""

import time
import argparse
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_settings, get_data_from_message, send_message

"""Создание сокета"""
s = socket(AF_INET, SOCK_STREAM)

"""Установка соединения"""
s.connect((get_settings()['host'], get_settings()['port']))

"""параметры командной строки скрипта client.py <addr> [<port>]:"""
parser = argparse.ArgumentParser(description='command line client parameters')
parser.add_argument('addr', type=str, help='server ip address')
parser.add_argument('port', type=int, nargs='?', default=7777, help='port')
args = parser.parse_args()
print(args)

"""Формирование presence-сообщение"""
msg = {
    "action": "presence",
    "time": time.ctime(time.time()),
    "type": "status",
    "user": {
        "account_name": "di-mario",
        "status": "Свободу Навальному!"
    }
}
"""Отправка presence-сообщение server"""
send_message(s, msg)

"""Получение ответа от сервера"""
print('Сообщение от сервера: ', get_data_from_message(s.recv(1000000)))

"""Соединение закрыто"""
s.close()


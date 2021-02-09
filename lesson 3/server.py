import argparse
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_settings, get_data_from_message,

"""Создание сокета"""
s = socket(AF_INET, SOCK_STREAM)

"""Привязка сокета к IP-адресу и порту"""
s.bind(('', get_settings()['port']))

"""Прием соединения"""
s.listen(4)

"""# параметры командной строки скрипта server.py -p <port>, -a <addr>:"""
parser = argparse.ArgumentParser(description='command line server parameters')
parser.add_argument('-a', '--addr', type=str, nargs='?', default='', help='ip address')
parser.add_argument('-p', '--port', type=int, nargs='?', default=7777, help='tcp-port')
args = parser.parse_args()
print(args)

while True:
    """Прием запроса на устанвку соединения"""
    client, addr = s.accept()

    """Прием сообщения client"""
    print('Сообщение: ', get_data_from_message(client.recv(1000000)), ',отправлено клиентом: ', addr)

    """Формирование ответа client"""
    msg = {
        "response": '200',
        "alert": 'Привет!Свободу подтверждаю)'
    }

    """Отправка ответа client"""
    send_message(client, msg)

    """Соединение закрыто"""
    client.close()


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

import json
import sys
import time
import argparse
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_configs, get_message, send_message
from log.client_log import client_logger
from log.log_decor import Log

CONFIGS = get_configs()


# функция формирует presence-сообщение
@Log('DEBUG')
def create_presence_message(CONFIGS):
    message = {
        CONFIGS.get('ACTION'): CONFIGS.get('PRESENCE'),
        CONFIGS.get('TIME'): time.ctime(time.time()),
        "type": "status",
        CONFIGS.get('USER'): {
            CONFIGS.get('ACCOUNT_NAME'): "di-mario",
            "status": "Привет, сервер!"
        }
    }
    return message


# функция проверки ответа сервера
@Log('DEBUG')
def check_response(message):
    if CONFIGS.get('RESPONSE') in message:
        if message[CONFIGS.get('RESPONSE')] == 200:
            client_logger.debug('ответ от сервера получен')
            return f'200: OK, {message[CONFIGS.get("ALERT")]}'
        client_logger.error('произошла ошибка ответа сервера')
        return f'400: {message[CONFIGS.get("ERROR")]}'
    raise ValueError


def main():
    responses = []
    # global CONFIGS
    # параметры командной строки скрипта client.py <addr> [<port>]:
    parser = argparse.ArgumentParser(description='command line client parameters')
    parser.add_argument('addr', type=str, nargs='?', default=CONFIGS.get('DEFAULT_IP_ADDRESS'),
                        help='server ip address')
    parser.add_argument('port', type=int, nargs='?', default=CONFIGS.get('DEFAULT_PORT'), help='port')
    args = parser.parse_args()
    print(args)

    # проверка введённых параметров из командной строки вызова клиента
    try:
        server_address = args.addr
        server_port = int(args.port)
        if not 65535 >= server_port >= 1024:
            raise ValueError
    except IndexError:
        server_address = CONFIGS.get('DEFAULT_IP_ADDRESS')
        server_port = CONFIGS.get('DEFAULT_PORT')
        client_logger.warning('Подставлены значения адреса и порта по умолчанию')
    except ValueError:
        # print('Порт должен быть указан в пределах от 1024 до 65535')
        client_logger.critical('Порт должен быть указан в пределах от 1024 до 65535')
        sys.exit(1)

    # При использовании оператора with сокет будет автоматически закрыт
    with socket(AF_INET, SOCK_STREAM) as sock:  # Создать сокет TCP
        # устанавливает соединение
        sock.connect((server_address, server_port))
        if 'send' in sys.argv:
            print('клиент в режиме отправки сообщения')
            while True:
                message_to_send = input("Введите сообщение (для выхода - 'q'): ")
                if message_to_send == 'q':
                    break
                sock.send(message_to_send.encode(CONFIGS.get('ENCODING')))
                data = sock.recv(CONFIGS.get('MAX_PACKAGE_LENGTH')).decode(CONFIGS.get('ENCODING'))
                print('Ответ: ', data)
        else:
            print('клиент в режиме слушателя')
            while True:
                data = sock.recv(CONFIGS.get('MAX_PACKAGE_LENGTH')).decode(CONFIGS.get('ENCODING'))
                if data:
                    responses.append(data)
                    print('Ответ: ', data)




    # # формирует и отправляет сообщение серверу;
    # presence_message = create_presence_message(CONFIGS)
    # send_message(s, presence_message, CONFIGS)
    #
    # # получает ответ сервера и проверяет сообщение сервера
    # try:
    #     response = get_message(s, CONFIGS)
    #     checked_response = check_response(response)
    #     print(f'Ответ от сервера: {checked_response}')
    # except (ValueError, json.JSONDecodeError):
    #     # print('Ошибка декорирования сообщения')
    #     client_logger.error('Ошибка декорирования сообщения')
    #
    # # закрывает соединение
    # s.close()


if __name__ == '__main__':
    main()

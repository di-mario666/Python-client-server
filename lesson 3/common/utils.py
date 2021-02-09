import json

"""перевода сообщения из байтов"""
def get_data_from_message(response):
    return json.loads(response.decode('utf-8'))


"""перевода сообщения в байтов"""
def send_message(socket, data_dict):
    socket.send(json.dumps(data_dict).encode('utf-8'))

"""получение словаря из json файла с настройками"""
def get_settings():
    with open('common/settings.json') as f_n:
        objs = json.load(f_n)
        return objs
"""1. Каждое из слов «разработка», «сокет», «декоратор» представить 
в строковом формате и проверить тип и содержание соответствующих переменных. 
Затем с помощью онлайн-конвертера преобразовать строковые представление 
в формат Unicode и также проверить тип и содержимое переменных."""
str_1 = "разработка"
str_2 = str('сокет')
str_3 = "декоратор"
print(type(str_1), type(str_2), type(str_3))

str_unic_1 = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"
str_unic_2 = "\u0441\u043e\u043a\u0435\u0442"
str_unic_3 = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"
print(str_unic_1, str_unic_2, str_unic_3)
print(type(str_unic_1), type(str_unic_2), type(str_unic_3))

"""2. Каждое из слов «class», «function», «method» записать 
в байтовом типе без преобразования в последовательность кодов 
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных."""
str_bytes_1 = b'class'
print(len(str_bytes_1), type(str_bytes_1))
str_bytes_2 = b'function'
print(len(str_bytes_2), type(str_bytes_2))
str_bytes_3 = b'method'
print(len(str_bytes_3), type(str_bytes_3))

"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""
# str_bytes_1 = b'класс'
# str_bytes_2 = b'функция'
# print(str_bytes_2, str_bytes_1)
"""Слова на кириллице невозможно перевести в байтовый тип,так как они не относятся к ASCII"""

"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» 
из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode)."""
str_1 = 'разработка'
enc_str_bytes_1 = str_1.encode('utf-8')
dec_str_1 = enc_str_bytes_1.decode('utf-8')

str_2 = 'администрирование'
enc_str_bytes_2 = str_2.encode('utf-8')
dec_str_2 = enc_str_bytes_2.decode('utf-8')

str_3 = 'protocol'
enc_str_bytes_3 = str_3.encode('utf-8')
dec_str_3 = enc_str_bytes_3.decode('utf-8')

str_4 = 'standard'
enc_str_bytes_4 = str_4.encode('utf-8')
dec_str_4 = enc_str_bytes_4.decode('utf-8')

print("Байтовое преобразование слов:\n", enc_str_bytes_1, enc_str_bytes_2, enc_str_bytes_3, enc_str_bytes_4)
print("Декодирование слов:\n", dec_str_1, dec_str_2, dec_str_3, dec_str_4)

"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и 
преобразовать результаты из байтовового в строковый тип на кириллице."""
import subprocess

args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line)

for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор». 
Проверить кодировку файла по умолчанию. 
Принудительно открыть файл в формате Unicode и вывести его содержимое."""

import locale
my_file = open("test_file.txt", "w+")
my_file.write("сетевое программирование\nсокет\nдекоратор\n")
my_file.close()

print('***********************')
with open('test_file.txt') as my_file:
    for el_str in my_file:
        print(el_str)
        el_str = el_str.encode('utf-8')
        print(el_str)


"""Проверка кодировки"""
def_coding = locale.getpreferredencoding()
print("Кодировка файла:", def_coding)


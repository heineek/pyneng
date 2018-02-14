# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP = '192.168.3.1'
IP_list = [int(octet) for octet in IP.split('.')]
output = """
{0:<8}   {1:<8}   {2:<8}   {3:<8}
{0:08b}   {1:08b}   {2:08b}   {3:08b}
""".format(IP_list[0], IP_list[1], IP_list[2], IP_list[3])

print(output)

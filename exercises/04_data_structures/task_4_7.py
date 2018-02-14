# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'
MAC_INT = int(MAC.replace(':', ''), 16)
MAC_BIN_STR = str(bin(MAC_INT))[2:]
print(MAC_BIN_STR)

# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

while True:
    ip = input("Enter IP address: ")
    try:
        if len(ip.split('.')) != 4:
            raise ValueError
        for byte in ip.split('.'):
            if int(byte) < 0 or int(byte) > 255:
                raise ValueError
    except ValueError:
        print("Incorrect IPv4 address")
    else:
        first = int(ip.split('.')[0])

        if ip == "0.0.0.0":
            result = 'unassigned'
        elif ip == "255.255.255.255":
            result = 'local broadcast'
        elif 1 <= first <= 223:
            result = 'unicast'
        elif 224 <= first <= 239:
            result = 'multicast'
        else:
            result = 'unused'

        print(result)
        break

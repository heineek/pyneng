# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
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

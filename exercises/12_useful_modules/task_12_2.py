# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''
from task_12_1 import check_ip_addresses


def check_ip_availabality(ip_range):
    if '-' in ip_range:
        first_ip, last_ip = ip_range.split('-')
        if '.' not in last_ip:
            last_ip = '.'.join(first_ip.split('.')[:3]) + '.' + last_ip
        first_ip_last_byte = int(first_ip.split('.')[-1])
        first_3_octets = '.'.join(first_ip.split('.')[:3])
        num_of_add = int(last_ip.split('.')[-1]) - first_ip_last_byte
        addresses = []
        for last_octet in range(first_ip_last_byte,
                                first_ip_last_byte+num_of_add+1):
            addresses.append(first_3_octets + '.{}'.format(str(last_octet)))
    else:
        addresses = [ip_range]

    return(check_ip_addresses(addresses))

print(check_ip_availabality('8.8.8.8'))
print(check_ip_availabality('8.8.8.8-10'))
print(check_ip_availabality('8.8.8.8-8.8.8.12'))

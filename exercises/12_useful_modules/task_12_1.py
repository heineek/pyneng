# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess


def check_ip_addresses(addresses):
    accessible = []
    inaccessible = []
    for address in addresses:
        result = subprocess.run(['ping', '-c', '3', address],
                                stdout=subprocess.DEVNULL)
        if result.returncode:
            inaccessible.append(address)
        else:
            accessible.append(address)
    return accessible, inaccessible

if __name__ == '__main__':
    addresses = ["172.20.5.133", "172.20.5.134", "8.8.8.8", "10.1.1.1",
                 "localhost"]
    print(check_ip_addresses(addresses))

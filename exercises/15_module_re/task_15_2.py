# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию return_match, которая ожидает два аргумента:
* имя файла, в котором находится вывод команды show
* регулярное выражение

Функция должна обрабатывать вывод команды show построчно и возвращать список подстрок,
которые совпали с регулярным выражением (не всю строку, где было найдено совпадение,
а только ту подстроку, которая совпала с выражением).

Проверить работу функции на примере вывода команды sh ip int br (файл sh_ip_int_br.txt).
Вывести список всех IP-адресов из вывода команды.

Соответственно, регулярное выражение должно описывать подстроку с IP-адресом (то есть, совпадением должен быть IP-адрес).


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re

def return_match(file, regexp):
    result = []
    with open(file, 'r') as f:
        for line in f:
            match = re.search(regexp, line)
            if match:
                result.append(match.group())
    return result

regexp = r'(\d{1,3}\.){3}\d{1,3}'
print(return_match('sh_ip_int_br.txt', regexp))

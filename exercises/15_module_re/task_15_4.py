# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''
import re
from pprint import pprint

def parse_sh_ip_int_br(output):
    regexp = '(?P<intf>\S+) +(?P<ip>\S+) +\w+ +\w+ (?P<status>(?:fuck)? ?up|down) +(?P<proto>up|down)'
    with open(output, 'r') as f:
        matches = re.finditer(regexp, f.read(), re.DOTALL)
        for match in matches:
            print(match.group())
            

pprint(parse_sh_ip_int_br('sh_ip_int_br_2.txt'))

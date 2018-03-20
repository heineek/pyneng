# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re
from pprint import pprint


def parse_cfg(config):
    interfaces = {}
    regexp = ('!\ninterface (?P<intf>\S+)'
              '| ip address (?P<ip>(?:\d+\.){3}\d+) (?P<mask>(?:\d+\.){3}\d+)')
    with open(config, 'r') as f:
        output = f.read()

    matches = re.finditer(regexp, output)
    for match in matches:
        if match.lastgroup == 'intf':
            interface = match.group(match.lastgroup)
            interfaces[interface] = None
        elif interface:
            interfaces[interface] = match.group('ip', 'mask')
    result = {key: interfaces[key] for key in interfaces if interfaces[key]}
    return result

pprint(parse_cfg('config_r1.txt'))

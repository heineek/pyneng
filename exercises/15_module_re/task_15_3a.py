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
    result = {}
    re_intf = r'interface (\S+)'
    re_add_mask = r'ip address ((?:\d+\.){3}\d+) ((?:\d+\.){3}\d+)'
    with open(config, 'r') as f:
        for line in f:
            match_intf = re.search(re_intf, line)
            if match_intf:
                result[match_intf.group(1)] = None
            match_add_mask = re.search(re_add_mask, line)
            if match_add_mask:
                result[match_intf.group(1)] = match_add_mask.groups()
    return result

pprint(parse_cfg('config_r1.txt'))

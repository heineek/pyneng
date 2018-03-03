# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re
from pprint import pprint

def parse_sh_cdp_neighbors(output):
    loc_host = re.search('(\w+)>', output).group(1)
    neighbors = {}
    # На данный момент в душе не ебу как быть с WS-C3750, чтобы он сука попадал под шаблон
    regexp = '(?P<rem_host>\S+) +(?P<loc_intf>\S+ ?\S+) +\d+ +.*?\d+ +(?P<rem_intf>\S+ ?\S+)'
    for line in output.split('\n'):
        match = re.search(regexp, line)
        if match:
            rem_host, loc_intf, rem_intf = match.groups()
            neighbors[loc_intf] = {rem_host: rem_intf}
    
    return {loc_host: neighbors}

if __name__ == "__main__":
    with open('sh_cdp_n_sw1.txt', 'r') as f:
        pprint(parse_sh_cdp_neighbors(f.read()))

# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def parse_cdp_neighbors(output):
    result = {}
    output_list = output.split('\n')
    local_device = output_list[0].split('>')[0]
    for line in output_list[3:]:
        fields = line.split()
        remote_device = fields[0]
        

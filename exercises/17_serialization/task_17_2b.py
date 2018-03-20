# -*- coding: utf-8 -*-
'''
Задание 17.2b

Переделать функциональность скрипта из задания 17.2a,
в функцию generate_topology_from_cdp.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_file - этот параметр управляет тем, будет ли записан в файл, итоговый словарь
 * значение по умолчанию - True
* topology_filename - имя файла, в который сохранится топология.
 * по умолчанию, должно использоваться имя topology.yaml.
 * топология сохраняется только, если аргумент save_to_file указан равным True

Функция возвращает словарь, который описывает топологию.
Словарь должен быть в том же формате, что и в задании 17.2a.

Проверить работу функции generate_topology_from_cdp на файлах:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Записать полученный словарь в файл topology.yaml.

Не копировать код функции parse_sh_cdp_neighbors
'''
from task_17_2 import parse_sh_cdp_neighbors
from pprint import pprint
import yaml


def generate_topology_from_cdp(list_of_files, save_to_file=True,
                               topology_filename='topology.yaml'):
    topology = {}

    for file in list_of_files:
        with open(file, 'r') as f:
            topology.update(parse_sh_cdp_neighbors(f.read()))

    if save_to_file:
        with open(topology_filename, 'w') as fw:
            yaml.dump(topology, fw)

    return topology

files = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt',
         'sh_cdp_n_r3.txt', 'sh_cdp_n_r4.txt', 'sh_cdp_n_r5.txt',
         'sh_cdp_n_r6.txt']

pprint(generate_topology_from_cdp(files, topology_filename='topology2.yaml'))

# -*- coding: utf-8 -*-
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology


def deduplicate_links(topology):
    '''
    if (X, Y): (N, M) and (N, M): (X, Y) are in the same dict, remove one of
    them
    '''
    result = topology.copy()

    # will change during dict changes in Python3
    keys = result.keys()
    values = result.values()

    for value in list(values):
        if value in keys and result[value] in keys:
            del(result[value])
    return result

files = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt',
         'sh_cdp_n_r3.txt']

topology = {}
for file in files:
    with open(file, 'r') as f:
        topology.update(parse_cdp_neighbors(f.read()))

draw_topology(deduplicate_links(topology))

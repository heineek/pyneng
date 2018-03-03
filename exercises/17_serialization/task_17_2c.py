# -*- coding: utf-8 -*-
'''
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
from draw_network_graph import draw_topology
import yaml
from pprint import pprint
from deduplicate_links import deduplicate_links

with open('topology.yaml', 'r') as f:
    topology = yaml.load(f)

topology_dict = {}  # ((device, loc_intf): (rem_device, rem_intf))
for device, neighbors in topology.items():
    for loc_intf, rem_neighbors in neighbors.items():
        for rem_device, rem_intf in rem_neighbors.items():
            topology_dict[(device, loc_intf)] = (rem_device, rem_intf)

draw_topology(deduplicate_links(topology_dict))

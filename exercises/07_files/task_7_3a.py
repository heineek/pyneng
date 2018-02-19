# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
lines = []
with open('CAM_table.txt', 'r') as f:
    lines = f.readlines()[6:]

output_list = []

for line in lines:
    fields = line.split()
    cleared_line = " {}    {}   {}".format(fields[0], fields[1], fields[3])
    output_list.append(cleared_line)

output_list.sort()
for line in output_list:
    print(line)

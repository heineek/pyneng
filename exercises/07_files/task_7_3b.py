# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan = input("Enter VLAN ID: ")
lines = []
with open('CAM_table.txt', 'r') as f:
    lines = f.readlines()[6:]

output_list = []

for line in lines:
    fields = line.split()
    if fields[0] == vlan:
        cleared_line = " {}    {}   {}".format(fields[0], fields[1], fields[3])
        print(cleared_line)
    

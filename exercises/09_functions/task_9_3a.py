# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def get_int_vlan_map(config):
    int_configs = {}
    with open(config, 'r') as f:
        for line in f:
            if line.startswith('interface'):
                curr_intf = line.split()[1]
                int_configs[curr_intf] = []
            elif line.startswith(' '):
                int_configs[curr_intf].append(line.strip())
            else:
                continue

    access_ports = {}
    trunk_ports = {}

    for intf, commands in int_configs.items():
        if "switchport mode access" in commands:
            for line in commands:
                if line.startswith("switchport access vlan"):
                    vlan = line.split()[-1]
                    break
            else:
                vlan = '1'
            access_ports[intf] = int(vlan)
        if "switchport mode trunk" in commands:
            for line in commands:
                if line.startswith("switchport trunk allowed vlan"):
                    vlans = [int(vlan) for vlan in line.split()[-1].split(',')]
                    break
            trunk_ports[intf] = vlans

    return access_ports, trunk_ports

print(get_int_vlan_map('config_sw2.txt'))

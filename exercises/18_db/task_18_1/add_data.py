# -*- coding: utf-8 -*-
'''
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''

import glob
import yaml
import re
import sqlite3

def add_switch_data():
    datafile = 'switches.yml'
    db_filename = 'dhcp_snooping.db'

    with open(datafile, 'r') as f:
        swiches = yaml.load(f)
        switch_data = [(hostname, location) for hostname, location in swiches['switches'].items()]
    
    con = sqlite3.connect(db_filename)
    
    try:
        with con:
            query = 'INSERT INTO switches VALUES (?, ?)'
            con.executemany(query, switch_data)
    except sqlite3.IntegrityError as e:
        print('Error occured: ', e)


def add_dhcp_snoop_data():
    db_filename = 'dhcp_snooping.db'
    dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

    dhcp_snoop_data = []        # (mac, ip, vlan, interface, hostname)
    regexp = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    for file in dhcp_snoop_files:
        hostname = re.search('(\w+?)_', file).group(1)
        with open(file, 'r') as f:
            for line in f:
                match = regexp.search(line)
                if match:
                    mac, ip, vlan, interface = match.groups()
                    dhcp_snoop_data.append((mac, ip, vlan, interface, hostname))
                    
    con = sqlite3.connect(db_filename)
    
    try:
        with con:
            query = 'INSERT INTO dhcp VALUES (?, ?, ?, ?, ?)'
            con.executemany(query, dhcp_snoop_data)
    except sqlite3.IntegrityError as e:
        print('Error occured: ', e)

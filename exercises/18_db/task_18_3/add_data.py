# -*- coding: utf-8 -*-
'''
Задание 18.1a

Скопировать скрипт add_data.py из задания 18.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''
import glob
import yaml
import re
import sqlite3
import os

datafile = 'switches.yml'
db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

def db_exist(db_filename):
    return os.path.exists(db_filename)


def add_switch_data():
    if db_exist(db_filename):
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
    else:
        print('Database file no found, create it first.')


def add_dhcp_snoop_data():
    if db_exist(db_filename):
        dhcp_snoop_data = []        # (mac, ip, vlan, interface, hostname, active)
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
                for entry in dhcp_snoop_data:
                    select_query = 'SELECT * FROM dhcp'
                    query_result = con.execute(select_query)
                    if ((*entry, 0)) in query_result or ((*entry, 1)) in query_result:
                        update_query = 'UPDATE dhcp SET active=1 WHERE mac="{}"'.format(entry[0])
                        con.execute(update_query)
                    else:
                        insert_query = 'INSERT INTO dhcp VALUES (?, ?, ?, ?, ?, ?)'
                        con.execute(insert_query, (*entry, 0))

        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)
    else:
        print('Database file not found, create it first.')


def get_snmp_snooping_data():
    con = sqlite3.connect(db_filename)
    select_query = 'SELECT * FROM dhcp'
    with con:
        query_result = con.execute(select_query)
    for row in query_result:
        print(row)


if __name__ == '__main__':
    # add_switch_data()
    add_dhcp_snoop_data()
    get_snmp_snooping_data()

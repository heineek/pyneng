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

def db_exist(db_filename):
    return os.path.exists(db_filename)

def add_switch_data():
    datafile = 'switches.yml'
    db_filename = 'dhcp_snooping.db'

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
    db_filename = 'dhcp_snooping.db'
    dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

    if db_exist(db_filename):
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
    else:
        print('Database file no found, create it first.')

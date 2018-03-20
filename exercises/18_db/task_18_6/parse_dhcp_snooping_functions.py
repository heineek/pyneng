import sqlite3
import os
import yaml
import datetime
import re


def create_db(name, schema):
    if not os.path.exists(name):
        con = sqlite3.connect(name)
        with con:
            with open(schema, 'r') as f:
                con.executescript(f.read())
    else:
        print('Database already exists.')


def add_data_switches(db_file, filename):
    if os.path.exists(db_file):
        for file in filename:
            with open(file, 'r') as f:
                swiches = yaml.load(f)
                switch_data = [(hostname, location) for hostname, location in swiches['switches'].items()]

        con = sqlite3.connect(db_file)

        try:
            with con:
                query = 'INSERT INTO switches VALUES (?, ?)'
                con.executemany(query, switch_data)
        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)
    else:
        print('Database file no found, create it first.')


def add_data(db_file, filename):
    if os.path.exists(db_file):
        dhcp_snoop_data = []        # (mac, ip, vlan, interface, hostname)
        regexp = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
        for file in filename:
            hostname = re.search('(\w+?)_', file).group(1)
            with open(file, 'r') as f:
                for line in f:
                    match = regexp.search(line)
                    if match:
                        mac, ip, vlan, interface = match.groups()
                        dhcp_snoop_data.append((mac, ip, vlan, interface, hostname))

        con = sqlite3.connect(db_file)

        try:
            with con:
                select_all_query = 'SELECT * FROM dhcp'
                cursor = con.cursor()
                result = cursor.execute(select_all_query)
                all_dhcp_snoop_macs = [entry[0] for entry in result]

                now = str(datetime.datetime.today().replace(microsecond=0))

                for entry in dhcp_snoop_data:
                    if entry[0] in all_dhcp_snoop_macs:
                        update_query = 'UPDATE dhcp SET active=1, last_active="{}" WHERE mac="{}"'.format(now, entry[0])
                        con.execute(update_query)
                        all_dhcp_snoop_macs.remove(entry[0])
                    else:
                        insert_query = 'INSERT INTO dhcp VALUES (?, ?, ?, ?, ?, ?, ?)'
                        con.execute(insert_query, (*entry, 0, now))

                    for mac in all_dhcp_snoop_macs:
                        update_query = 'UPDATE dhcp SET active=0 WHERE mac="{}"'.format(mac)
                        con.execute(update_query)

        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)
    else:
        print('Database file not found, create it first.')


def get_data(db_file, key, value):
    keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
    if key not in keys:
        print('Данный параметр не поддерживается')
        return
    keys.remove(key)

    conn = sqlite3.connect(db_file)

    # Позволяет далее обращаться к данным в колонках, по имени колонки
    conn.row_factory = sqlite3.Row

    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)

    query_for_active = 'SELECT * FROM dhcp WHERE {} = ? AND active=1'.format(key)
    result_for_active = conn.execute(query_for_active, (value, ))
    query_for_inactive = 'SELECT * FROM dhcp WHERE {} = ? AND active=0'.format(key)
    result_for_inactive = conn.execute(query_for_inactive, (value, ))

    for row in result_for_active:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)

    if result_for_inactive:
        print('\n' + '-' * 40)
        print('Inactive values:\n' + '-' * 40)
        for row in result_for_inactive:
            for k in keys:
                print('{:12}: {}'.format(k, row[k]))
            print('-' * 40)


def get_all_data(db_file):
    conn = sqlite3.connect(db_file)
    query_for_active = 'SELECT * FROM dhcp WHERE active=1'
    query_for_inactive = 'SELECT * FROM dhcp WHERE active=0'
    cursor = conn.cursor()

    print('-' * 85)
    print('Active values:')
    print('-' * 85)

    for row in cursor.execute(query_for_active):
        print('{}  {:15}     {:4}   {:16}     {}         {}'.format(*row))
    print('-' * 85)

    inactive_entries = cursor.execute(query_for_inactive)
    if inactive_entries:
        print('Inactive values:')
        print('-' * 85)
        for row in inactive_entries:
            print('{}  {:15}     {:4}   {:16}     {}         {}'.format(*row))

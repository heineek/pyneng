# -*- coding: utf-8 -*-
'''
На основе файла get_data_ver1.py из раздела, создать скрипт get_data.py.

Код в скрипте должен быть разбит на функции. Какие именно функции и как разделить код, надо решить самостоятельно. Часть кода может быть глобальной.

В примере из раздела, скрипту передавались два аргумента:

key - имя столбца, по которому надо найти информацию
value - значение
Теперь необходимо расширить функциональность таким образом:

если скрипт был вызван без аргументов, вывести всё содержимое таблицы dhcp
отформатировать вывод в виде столбцов
если скрипт был вызван с двумя аргументами, вывести информацию из таблицы dhcp, которая соответствует полю и значению
если скрипт был вызван с любым другим количеством аргументов, вывести сообщение, что скрипт поддерживает только два или ноль аргументов
Обработка некорректного ввода аргумента будет выполняться в следующем задании

Файл БД можно скопировать из прошлых заданий

В итоге, вывод должен выглядеть так:

$ python get_data.py

В таблице dhcp такие записи:
----------------------------------------------------------------------
00:09:BB:3D:D6:58  10.1.10.2         10    FastEthernet0/1      sw1
00:04:A3:3E:5B:69  10.1.5.2          5     FastEthernet0/10     sw1
00:05:B3:7E:9B:60  10.1.5.4          5     FastEthernet0/9      sw1
00:07:BC:3F:A6:50  10.1.10.6         10    FastEthernet0/3      sw1
00:09:BC:3F:A6:50  192.168.1.100     100   FastEthernet0/5      sw1
00:A9:BB:3D:D6:58  10.1.10.20        10    FastEthernet0/7      sw2
00:B4:A3:3E:5B:69  10.1.5.20         5     FastEthernet0/5      sw2
00:C5:B3:7E:9B:60  10.1.5.40         5     FastEthernet0/9      sw2
00:A9:BC:3F:A6:50  100.1.1.6         3     FastEthernet0/20     sw3

$ python get_data.py ip 10.1.10.2

Detailed information for host(s) with ip 10.1.10.2
----------------------------------------
mac         : 00:09:BB:3D:D6:58
vlan        : 10
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------


$ python get_data.py vlan 10

Detailed information for host(s) with vlan 10
----------------------------------------
mac         : 00:09:BB:3D:D6:58
ip          : 10.1.10.2
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------
mac         : 00:07:BC:3F:A6:50
ip          : 10.1.10.6
interface   : FastEthernet0/3
switch      : sw1
----------------------------------------
mac         : 00:A9:BB:3D:D6:58
ip          : 10.1.10.20
interface   : FastEthernet0/7
switch      : sw2
----------------------------------------

$ python get_data.py vlan
Пожалуйста, введите два или ноль аргументов
'''
# -*- coding: utf-8 -*-
import sqlite3
import sys

db_filename = 'dhcp_snooping.db'

def get_filtered_data(key, value):
    keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
    if key not in keys:
        print('Данный параметр не поддерживается')
        return
    keys.remove(key)

    conn = sqlite3.connect(db_filename)

    #Позволяет далее обращаться к данным в колонках, по имени колонки
    conn.row_factory = sqlite3.Row

    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)

    query = 'select * from dhcp where {} = ?'.format(key)
    result = conn.execute(query, (value, ))

    for row in result:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)


def get_all_data():
    conn = sqlite3.connect(db_filename)
    query = 'SELECT * FROM dhcp'
    cursor = conn.cursor()

    print('В таблице dhcp такие записи:')
    print('-' * 70)
    
    for row in cursor.execute(query):
        print('{}  {:15}     {:4}   {:16}     {}'.format(*row))


if len(sys.argv) == 1:
    get_all_data()
elif len(sys.argv) == 3:
    key, value = sys.argv[1:]
    get_filtered_data(key, value)
else:
    print('Введите ноль или два аргумента.')

# -*- coding: utf-8 -*-
'''
Задание 18.1a

Скопировать скрипт add_data.py из задания 18.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''
from add_data import add_dhcp_snoop_data, add_switch_data

add_switch_data()
add_dhcp_snoop_data()

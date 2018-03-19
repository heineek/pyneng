# -*- coding: utf-8 -*-
'''
Задание 19.4

Создать функцию send_commands_to_devices (для подключения по SSH используется netmiko).

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В этой функции должен использоваться список словарей, в котором не указаны имя пользователя, пароль, и пароль на enable (файл devices2.yaml).

Функция должна запрашивать имя пользователя, пароль и пароль на enable при старте.
Пароль не должен отображаться при наборе.

Функция send_commands_to_devices должна использовать функцию send_commands из задания 19.3.

'''
import yaml, getpass
from pprint import pprint
from task_19_3 import send_commands

def send_commands_to_devices(devices_list, show='', filename='', config=None):
    user = input('Username: ')
    password = getpass.getpass('Password: ')
    enable = getpass.getpass('Enable password: ')

    result = []
    for device in devices_list:
        dev = device.copy()
        dev['username'] = user
        dev['password'] = password
        dev['secret'] = enable

        result.append(send_commands(dev, show, filename, config))
    
    return result


with open('devices2.yaml', 'r') as f:
    devices = yaml.load(f.read())
    devices_list = devices['routers']

commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]
command = 'sh ip int br'
filename = 'config.txt'

pprint(send_commands_to_devices(devices_list, show=command))
pprint(send_commands_to_devices(devices_list, filename=filename))
pprint(send_commands_to_devices(devices_list, config=commands))

# -*- coding: utf-8 -*-
'''
Задание 19.4a

Дополнить функцию send_commands_to_devices таким образом, чтобы перед подключением к устройствам по SSH,
выполнялась проверка доступности устройства pingом (можно вызвать команду ping в ОС).

> Как выполнять команды ОС, описано в разделе [subprocess](../../book/12_useful_modules/subprocess.md). Там же есть пример функции с отправкой ping.

Если устройство доступно, можно выполнять подключение.
Если не доступно, вывести сообщение о том, что устройство с определенным IP-адресом недоступно
и не выполнять подключение к этому устройству.

Для удобства можно сделать отдельную функцию для проверки доступности
и затем использовать ее в функции send_commands_to_devices.

'''
import yaml, getpass
from pprint import pprint
from task_19_3 import send_commands
from task_19_3b import is_accessible

def send_commands_to_devices(devices_list, show='', filename='', config=None):
    user = input('Username: ')
    password = getpass.getpass('Password: ')
    enable = getpass.getpass('Enable password: ')

    result = []
    for device in devices_list:
        if is_accessible(device['ip']):
            dev = device.copy()
            dev['username'] = user
            dev['password'] = password
            dev['secret'] = enable

            result.append(send_commands(dev, show, filename, config))
        else:
            print('Device with ip address {} is not accessible'.format(device['ip']))
    
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

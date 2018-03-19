# -*- coding: utf-8 -*-
'''
Задание 19.3b


Дополнить функцию send_commands таким образом, чтобы перед подключением к устройствам по SSH,
выполнялась проверка доступности устройства pingом (можно вызвать команду ping в ОС).

> Как выполнять команды ОС, описано в разделе 11_modules/subprocess.html. Там же есть пример функции с отправкой ping.

Если устройство доступно, можно выполнять подключение.
Если не доступно, вывести сообщение о том, что устройство с определенным IP-адресом недоступно
и не выполнять подключение  к этому устройству.

Для удобства можно сделать отдельную функцию для проверки доступности
и затем использовать ее в функции send_commands.
'''
import subprocess
import netmiko, yaml
from pprint import pprint
from task_19_1 import send_show_command
from task_19_2 import send_config_commands


def is_accessible(ip):
    result = subprocess.run(['ping', '-n', '3', ip], stdout=subprocess.DEVNULL)
    return False if result.returncode else True


def send_commands_from_file(device, filename):
    result = {}
    with open(filename, 'r') as f:
        commands = f.read()
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result[device['ip']] = ssh.send_config_set(commands)

    return result


def send_commands(device, show='', filename='', config=None):
    if show:
        return send_show_command(device, show)
    elif filename:
        return send_commands_from_file(device, filename)
    else:
        return send_config_commands(device, config)

if __name__ == '__main__':
    commands = [
        'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
    ]
    command = 'sh ip int br'
    
    with open('devices.yaml', 'r') as f:
        devices = yaml.load(f.read())
        device_list = devices['routers']
    
    for device in device_list:
        if is_accessible(device['ip']):
            print('show\n')
            pprint(send_commands(device, show=command))
            print('filename\n')
            pprint(send_commands(device, filename='config.txt'))
            print('config\n')
            pprint(send_commands(device, config=commands))
        else:
            print('Device with IP address {} is not accessible'.format(device['ip']))

# -*- coding: utf-8 -*-
'''
Задание 19.2a

Дополнить функцию send_config_commands из задания 19.2

Добавить аргумент verbose, который контролирует будет ли результат
выполнения команд выводится на стандартный поток вывода.

По умолчанию, результат должен выводиться.
'''
import netmiko, yaml
from pprint import pprint

def send_config_commands(device_params, commands, verbose=True):
    result = {}
    with netmiko.ConnectHandler(**device_params) as ssh:
        ssh.enable()
        result[device_params['ip']] = ssh.send_config_set(commands)
        if verbose:
            print(result[device_params['ip']])

    return result

commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']

with open('devices.yaml', 'r') as f:
        devices = yaml.load(f.read())

for device in devices['routers']:
    send_config_commands(device, commands, verbose=False)

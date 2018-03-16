# -*- coding: utf-8 -*-
'''
Задание 19.2

Создать функцию send_config_commands

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет перечень команд в конфигурационном режиме на основании переданных аргументов.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* config_commands - список команд, которые надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Отправить список команд commands на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_config_commands.

'''
import netmiko, yaml
from pprint import pprint

def send_config_commands(device_params, commands):
    result = {}
    with netmiko.ConnectHandler(**device_params) as ssh:
        ssh.enable()
        result[device_params['ip']] = ssh.send_config_set(commands)

    return result

commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']

with open('devices.yaml', 'r') as f:
        devices = yaml.load(f.read())

for device in devices['routers']:
    pprint(send_config_commands(device, commands))

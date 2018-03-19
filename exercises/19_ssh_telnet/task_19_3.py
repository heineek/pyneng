# -*- coding: utf-8 -*-
'''
Задание 19.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к устройству, которому надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри.
При вызове функции, всегда будет передаваться только один из аргументов show, config, filename.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 19.1
* config - функция send_config_commands из задания 19.2
* filename - функция send_commands_from_file (ее надо написать по аналогии с предыдущими)

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Проверить работу функции на примере:
* устройств из файла devices.yaml (для этого надо считать информацию из файла)
* и различных комбинация аргумента с командами:
    * списка команд commands
    * команды command
    * файла config.txt

'''
import netmiko, yaml
from pprint import pprint
from task_19_1 import send_show_command
from task_19_2 import send_config_commands

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
        print('show\n')
        pprint(send_commands(device, show=command))
        print('filename\n')
        pprint(send_commands(device, filename='config.txt'))
        print('config\n')
        pprint(send_commands(device, config=commands))

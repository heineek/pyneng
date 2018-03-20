# -*- coding: utf-8 -*-
'''
Задание 19.2d

В этом задании надо создать функцию send_cfg_to_devices, которая выполняет команды на нескольких устройствах последовательно и при этом выполняет проверку на ошибки в командах.

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* config_commands - список команд, которые надо выполнить

Функция должна проверять результат на такие ошибки:
* Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка, функция должна выводить сообщение на стандартный поток вывода с информацией о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

После обнаружения ошибки, функция должна спросить пользователя надо ли выполнять эту команду на других устройствах.

Варианты ответа [y]/n:
* y - выполнять команду на оставшихся устройствах (значение по умолчанию)
* n - не выполнять команду на оставшихся устройствах

Функция send_cfg_to_devices должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - IP устройства
* значение - вложенный словарь:
  * ключ - команда
  * значение - вывод с выполнением команд

В файле задания заготовлены команды с ошибками и без:
'''
import netmiko
import yaml
from pprint import pprint
from task_19_2c import send_config_commands


def send_cfg_to_devices(devices_list, config_commands):
    result_correct = {}
    result_incorrect = {}
    for device in devices_list:
        ip = device['ip']
        result_correct[ip], result_incorrect[ip] = \
            send_config_commands(device, commands, verbose=False)
    return result_correct, result_incorrect


commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

with open('devices.yaml', 'r') as f:
    devices = yaml.load(f.read())

pprint(send_cfg_to_devices(devices['routers'], commands))

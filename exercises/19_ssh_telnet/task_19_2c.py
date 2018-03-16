# -*- coding: utf-8 -*-
'''
Задание 19.2c

Переделать функцию send_config_commands из задания 19.2b

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды (значение по умолчанию)
* n - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками


Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить функцию на командах с ошибкой.

'''
import netmiko, yaml
from pprint import pprint

def send_config_commands(device_params, commands, verbose=True):
    result_correct = {}
    result_incorrect = {}
    
    with netmiko.ConnectHandler(**device_params) as ssh:
        ssh.enable()
        ssh.config_mode()
        result_incorrect[device_params['ip']] = ''
        result_correct[device_params['ip']] = ''
        for command in commands:
            result = ssh.send_command(command)
            if result.startswith('% ') or '^' in result:
                result_incorrect[device_params['ip']] += command + '\n' + result
                output = 'Error with command "{}" on device {}: {}'.format(
                    command, device_params['ip'], result[2:])
                print(output)
            else:
                result_correct[device_params['ip']] += command + '\n' + result
                if verbose:
                    pprint(result_correct[device_params['ip']])

    return result_correct, result_incorrect

commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

with open('devices.yaml', 'r') as f:
        devices = yaml.load(f.read())

for device in devices['routers']:
    pprint(send_config_commands(device, commands, verbose=False))

# -*- coding: utf-8 -*-
'''
Задание 19.2b

В этом задании необходимо переделать функцию send_config_commands из задания 19.2a или 19.2 и добавить проверку на ошибки.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

При этом, параметр verbose также должен работать, но теперь он отвечает за вывод
только тех команд, которые выполнились корректно.

Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Отправить список команд commands на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_config_commands.

Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#i
% Ambiguous command:  "i"

В файле задания заготовлены команды с ошибками и без:
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

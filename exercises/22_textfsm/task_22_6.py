# -*- coding: utf-8 -*-
'''
Задание 22.6

Это задание похоже на задание 22.5, но в этом задании подключения надо выполнять параллельно с помощью потоков.
Для параллельного подключения использовать модуль concurrent.futures.

В этом упражнении нужно создать функцию send_and_parse_command_parallel:
* она должна использовать внутри себя функцию send_and_parse_command
* какие аргументы должны быть у функции send_and_parse_command_parallel, нужно решить самостоятельно
* функция send_and_parse_command_parallel должна возвращать словарь, в котором:
 * ключ - IP устройства
 * значение - список словарей

Проверить работу функции send_and_parse_command_parallel на команде sh ip int br.

'''
from concurrent.futures import ThreadPoolExecutor, as_completed
from task_22_5 import send_and_parse_command
from pprint import pprint
import yaml


def send_and_parse_command_parallel(function, devices, attributes, index='index',
                           templates='templates', limit=2):
    result = {}
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_send_command = [
            executor.submit(function, device, attributes, index='index',
                            templates='templates') for device in devices['routers']]
        for f in as_completed(future_send_command):
            result.update(f.result())
    return result

test_command = "sh ip int br"
devices = yaml.load(open('devices.yaml'))
attributes = {'Command': test_command, 'Vendor': 'cisco_ios'}

pprint(send_and_parse_command_parallel(send_and_parse_command, devices,
                                       attributes))

# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_commands_threads, которая запускает функцию send_commands из задания 19.3 на разных устройствах в параллельных потоках.

Параметры функции send_commands_threads надо определить самостоятельно.
Должна быть возможность передавать параметры show, config, filename функции send_commands.

Функция send_commands_threads возвращает словарь с результатами выполнения команд на устройствах:

* ключ - IP устройства
* значение - вывод с выполнением команд

'''
from task_19_3 import send_commands
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import yaml


def send_commands_threads(function, devices, limit=2, show='', filename='', config=None):
    result = {}
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_send_command = [
            executor.submit(function, device, show, filename, config) for device in devices]
        for f in as_completed(future_send_command):
            result.update(f.result())
    return result


with open('devices.yaml', 'r') as f:
    devices = yaml.load(f.read())['routers']

pprint(send_commands_threads(send_commands, devices, show='sh clock', limit=3))

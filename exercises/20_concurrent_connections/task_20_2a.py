# -*- coding: utf-8 -*-
'''
Задание 20.2a

Переделать функцию send_commands_threads из задания 20.2 таким образом, чтобы с помощью аргумента limit, можно было указывать сколько подключений будут выполняться параллельно.

По умолчанию, значение аргумента должно быть 2.

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

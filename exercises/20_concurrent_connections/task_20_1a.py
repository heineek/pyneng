# -*- coding: utf-8 -*-
'''
Задание 20.1a

Переделать функцию из задания 20.1 таким образом,
чтобы она позволяла контролировать количество параллельных проверок IP.

Для этого, необходимо добавить новый параметр limit,
со значением по умолчанию - 2.

Функция должна проверять адреса из списка
таким образом, чтобы в любой момент времени максимальное количество
параллельных проверок было равным limit.

'''
import yaml
import getpass
import netmiko
import subprocess
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor, as_completed


def send_commands(device, show='', filename='', config=None):
    if show:
        return send_show_command(device, show)
    elif filename:
        return send_commands_from_file(device, filename)
    else:
        return send_config_commands(device, config)


def send_commands_from_file(device, filename):
    result = {}
    with open(filename, 'r') as f:
        commands = f.read()
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result[device['ip']] = ssh.send_config_set(commands)

    return result


def send_config_commands(device_params, commands):
    result = {}
    with netmiko.ConnectHandler(**device_params) as ssh:
        ssh.enable()
        result[device_params['ip']] = ssh.send_config_set(commands)

    return result


def send_show_command(device_params, command):
    result = {}
    with netmiko.ConnectHandler(**device_params) as ssh:
        result[device_params['ip']] = ssh.send_command(command)

    return result


def is_accessible(ip):
    result = subprocess.run(['ping', '-n', '3', ip], stdout=subprocess.DEVNULL)
    return (ip, False) if result.returncode else (ip, True)


def threads_ping(function, devices, limit=3):
    all_results = {}
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ping = [
            executor.submit(function, device['ip']) for device in devices
        ]
        for f in as_completed(future_ping):
            ip, is_accessible = f.result()
            all_results[ip] = is_accessible
    return all_results


def send_commands_to_devices(devices_list, show='', filename='', config=None):
    user = input('Username: ')
    password = getpass.getpass('Password: ')
    enable = getpass.getpass('Enable password: ')

    result = []
    for device in devices_list:
        dev = device.copy()
        dev['username'] = user
        dev['password'] = password
        dev['secret'] = enable
        result.append(send_commands(dev, show, filename, config))

    return result


with open('devices.yaml', 'r') as f:
    devices = yaml.load(f.read())
    devices_list = devices['routers']

commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]
command = 'sh ip int br'
filename = 'config.txt'


accessibility = threads_ping(is_accessible, devices_list)
accessible_devices = [device for device in devices_list if accessibility[device['ip']]]

pprint(send_commands_to_devices(accessible_devices, show=command))
pprint(send_commands_to_devices(accessible_devices, filename=filename))
pprint(send_commands_to_devices(accessible_devices, config=commands))

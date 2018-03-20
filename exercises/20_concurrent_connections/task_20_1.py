# -*- coding: utf-8 -*-
'''
Задание 20.1

Переделать задание 19.4a таким образом, чтобы проверка доступности устройств
выполнялась не последовательно, а параллельно.

Для этого, можно взять за основу функцию check_ip_addresses из задания 11.3.
Функцию надо переделать таким образом, чтобы проверка IP-адресов выполнялась
параллельно в разных потоках.

'''
import yaml, getpass
from pprint import pprint
from task_19_3 import send_commands
from concurrent.futures import ThreadPoolExecutor

def is_accessible(ip):
    result = subprocess.run(['ping', '-n', '3', ip], stdout=subprocess.DEVNULL)
    return {ip: False} if result.returncode else {ip: True}


def threads_conn(function, devices, limit=2):
    all_results = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ping = [
            executor.submit(function, device['ip']) for device in devices
        ]
        for f in as_completed(future_telnet):
            all_results.append(f.result())
    return all_results
    

def send_commands_to_devices(devices_list, show='', filename='', config=None):
    user = input('Username: ')
    password = getpass.getpass('Password: ')
    enable = getpass.getpass('Enable password: ')

    result = []
    for device in devices_list:
        if is_accessible(device['ip']):
            dev = device.copy()
            dev['username'] = user
            dev['password'] = password
            dev['secret'] = enable

            result.append(send_commands(dev, show, filename, config))
        else:
            print('Device with ip address {} is not accessible'.format(device['ip']))
    
    return result


with open('devices2.yaml', 'r') as f:
    devices = yaml.load(f.read())
    devices_list = devices['routers']

commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]
command = 'sh ip int br'
filename = 'config.txt'

pprint(send_commands_to_devices(devices_list, show=command))
pprint(send_commands_to_devices(devices_list, filename=filename))
pprint(send_commands_to_devices(devices_list, config=commands))

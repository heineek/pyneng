# -*- coding: utf-8 -*-
'''
Задание 19.1b

Дополнить функцию send_show_command из задания 19.1a таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
'''
import netmiko, yaml
from pprint import pprint

def send_show_command(device_params, command):
    result = {}
    try:
        with netmiko.ConnectHandler(**device_params) as ssh:
            result[device_params['ip']] = ssh.send_command(command)
    except netmiko.ssh_exception.NetMikoAuthenticationException as ex:
        print(ex)
    except netmiko.ssh_exception.NetMikoTimeoutException as ex:
        print(ex)
    else:
        return result

command = 'sh ip int br'

with open('devices.yaml', 'r') as f:
        devices = yaml.load(f.read())

for device in devices['routers']:
    pprint(send_show_command(device, command))

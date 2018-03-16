# -*- coding: utf-8 -*-
'''
Задание 19.1a

Переделать функцию send_show_command из задания 19.1 таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
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
    else:
        return result

command = 'sh ip int br'

with open('devices.yaml', 'r') as f:
        devices = yaml.load(f.read())

for device in devices['routers']:
    pprint(send_show_command(device, command))

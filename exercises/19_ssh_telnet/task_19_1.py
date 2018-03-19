# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - результат выполнения команды

Отправить команду command на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_show_command.

'''
import netmiko, yaml
from pprint import pprint

def send_show_command(device_params, command):
    result = {}
    with netmiko.ConnectHandler(**device_params) as ssh:
        result[device_params['ip']] = ssh.send_command(command)

    return result

if __name__ == '__main__':
    command = 'sh ip int br'
    
    with open('devices.yaml', 'r') as f:
            devices = yaml.load(f.read())
    
    for device in devices['routers']:
        pprint(send_show_command(device, command))

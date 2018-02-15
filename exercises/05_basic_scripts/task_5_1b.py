# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

prefix = argv[1]
host, length = prefix.split('/')
host_octets = [int(octet) for octet in host.split('.')]
mask_bin = '1' * int(length) + '0' * (32 - int(length))
mask_octets = [int(octet, 2) for octet in\
               [mask_bin[0:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:]]]
net_octets = [host_octet & mask_octet for host_octet, mask_octet in zip(host_octets, mask_octets)]

output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<9}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{mask_len}
{4:<8}  {5:<8}  {6:<8}  {7:<8}
{4:08b}  {5:08b}  {6:08b}  {7:08b}
""".format(net_octets[0], net_octets[1], net_octets[2], net_octets[3],\
            mask_octets[0], mask_octets[1], mask_octets[2], mask_octets[3],\
            mask_len=int(length))

print(output)

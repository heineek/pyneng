# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес
сети, то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и
маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
prefix = input("Enter network prefix: ")
host, length = prefix.split('/')
host_octets = [int(octet) for octet in host.split('.')]
mask_bin = '1' * int(length) + '0' * (32 - int(length))
mask_octets = [int(octet, 2) for octet in
               [mask_bin[0:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:]]]
net_octets = [host_octet & mask_octet for host_octet, mask_octet in
              zip(host_octets, mask_octets)]

output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<9}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{mask_len}
{4:<8}  {5:<8}  {6:<8}  {7:<8}
{4:08b}  {5:08b}  {6:08b}  {7:08b}
""".format(net_octets[0], net_octets[1], net_octets[2], net_octets[3],
           mask_octets[0], mask_octets[1], mask_octets[2], mask_octets[3],
           mask_len=int(length))

print(output)

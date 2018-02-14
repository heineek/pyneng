# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route_info = ospf_route.split()
ospf_route_info[0] = 'OSPF'
ospf_route_info[2] = ospf_route_info[2].strip('[]')

output = """
Protocol:             {proto}
Prefix:               {prfx}
AD/Metric:            {metric}
Next-Hop:             {nh}
Last update:          {last_upd}
Outbound Interface:   {out_intf}
""".format(proto=ospf_route_info[0], prfx=ospf_route_info[1], metric = ospf_route_info[2],
            nh=ospf_route_info[4], last_upd=ospf_route_info[5], out_intf=ospf_route_info[6])

print(output)

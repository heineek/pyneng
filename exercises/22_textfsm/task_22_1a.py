# -*- coding: utf-8 -*-
'''
Задание 22.1a

Переделать функцию parse_output из задания 22.1 таким образом,
чтобы, вместо списка списков, она возвращала один список словарей:
* ключи - названия столбцов,
* значения, соответствующие значения в столбцах.

То есть, для каждой строки будет один словарь в списке.
'''
import sys
import textfsm
from pprint import pprint


def parse_output(template, output):
    with open(template) as f, open(output) as output:
        re_table = textfsm.TextFSM(f)
        header = re_table.header
        parse_result = re_table.ParseText(output.read())
        result = [dict(zip(header, values)) for values in parse_result]
    return result


template = sys.argv[1]
output_file = sys.argv[2]

pprint(parse_output(template, output_file))

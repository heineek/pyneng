# -*- coding: utf-8 -*-
'''
Задание 22.4a

Переделать функцию из задания 22.4:
* добавить аргумент show_output, который контролирует будет ли выводится результат обработки команды на стандартный поток вывода
 * по умолчанию False, что значит результат не будет выводиться
* результат должен отображаться с помощью FormattedTable (пример есть в разделе)

'''
import clitable
from pprint import pprint


def parse_command_dynamic(attributes, output, index='index',
                          templates='templates', show_output=False):
    cli_table = clitable.CliTable(index, templates)
    attributes = attributes

    cli_table.ParseCmd(output, attributes)

    if show_output:
        print(cli_table.FormattedTable())

    data_rows = [list(row) for row in cli_table]
    header = list(cli_table.header)
    result = [dict(zip(header, row)) for row in data_rows]
    return result

output_sh_ip_int_br = open('output/sh_ip_int_br.txt').read()
attributes = {'Command': 'sh ip int br', 'Vendor': 'cisco_ios'}

pprint(parse_command_dynamic(attributes, output_sh_ip_int_br, show_output=True))

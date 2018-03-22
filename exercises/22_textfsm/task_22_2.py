# -*- coding: utf-8 -*-
'''
Задание 22.2

В этом задании нужно использовать функцию parse_output из задания 22.1.
Она используется для того, чтобы получить структурированный вывод
в результате обработки вывода команды.

Полученный вывод нужно записать в CSV формате.

Для записи вывода в CSV, нужно создать функцию list_to_csv, которая ожидает как аргументы:
* список:
 * первый элемент - это список с названиями заголовков
 * остальные элементы это списки, в котором находятся результаты обработки вывода
* имя файла, в который нужно записать данные в CSV формате

Проверить работу функции на примере обработки
команды sh ip int br (шаблон и вывод есть в разделе).
'''
from task_22_1 import parse_output
import csv


def list_to_csv(data, outfile):
    with open(outfile, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        writer.writerows(data)

data = parse_output('templates\\sh_ip_int_br.template', 'output\\sh_ip_int_br.txt')
outfile = 'sh_ip_int_br.csv'
list_to_csv(data, outfile)

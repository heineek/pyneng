# -*- coding: utf-8 -*-
'''
Задание 21.1b

Дополнить функцию generate_cfg_from_template из задания 21.1 или 21.1a:
* добавить поддержку разных форматов для файла с данными

Должны поддерживаться такие форматы:
* YAML
* JSON
* словарь Python

Сделать для каждого формата свой параметр функции.
Например:
* YAML - yaml_file
* JSON - json_file
* словарь Python - py_dict

Проверить работу функции на шаблоне templates/for.txt и данных:
* data_files/for.yml
* data_files/for.json
* словаре data_dict

'''
from jinja2 import Environment, FileSystemLoader
import yaml
import json
import os


def generate_cfg_from_template(template_path, trim_blocks=True,
                               lstrip_blocks=True, yaml_file='', json_file='',
                               py_dict=''):
    template_dir, template_file = os.path.split(template_path)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=trim_blocks,
        lstrip_blocks=lstrip_blocks)
    template = env.get_template(template_file)
    
    if yaml_file:
        vars_dict = yaml.load(open(yaml_file))
    elif json_file:
        vars_dict = json.load(open(json_file))
    elif py_dict:
        vars_dict = data_dict
    else:
        print('No data file specified!')
        return 
    
    return template.render(vars_dict)

template_path = 'templates\\for.txt'

data_dict = {
    'vlans': {
        10: 'Marketing',
        20: 'Voice',
        30: 'Management'
    },
    'ospf': [{
        'network': '10.0.1.0 0.0.0.255',
        'area': 0
    }, {
        'network': '10.0.2.0 0.0.0.255',
        'area': 2
    }, {
        'network': '10.1.1.0 0.0.0.255',
        'area': 0
    }],
    'id': 3,
    'name': 'R3'
}

print(generate_cfg_from_template(template_path, yaml_file='data_files\\for.yml'))
print('\n\n')
print(generate_cfg_from_template(template_path, json_file='data_files\\for.json'))
print('\n\n')
print(generate_cfg_from_template(template_path, py_dict=data_dict))

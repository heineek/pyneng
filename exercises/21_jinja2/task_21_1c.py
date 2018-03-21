# -*- coding: utf-8 -*-
'''
Задание 21.1c

Переделать функцию generate_cfg_from_template из задания 21.1, 21.1a или 21.1b:
* сделать автоматическое распознавание разных форматов для файла с данными
* для передачи разных типов данных, должен использоваться один и тот же параметр data

Должны поддерживаться такие форматы:
* YAML - файлы с расширением yml или yaml
* JSON - файлы с расширением json
* словарь Python

Если не получилось определить тип данных, вывести сообщение error_message (перенести текст сообщения в тело функции), завершить работу функции и вернуть None.

Проверить работу функции на шаблоне templates/for.txt и данных:
* data_files/for.yml
* data_files/for.json
* словаре data_dict

'''
from jinja2 import Environment, FileSystemLoader
import yaml
import json
import os


def generate_cfg_from_template(template_path, data, trim_blocks=True,
                               lstrip_blocks=True):
    template_dir, template_file = os.path.split(template_path)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=trim_blocks,
        lstrip_blocks=lstrip_blocks)
    template = env.get_template(template_file)

    error_message = '''
                    Не получилось определить формат данных.
                    Поддерживаются файлы с расширением .json, .yml, .yaml и словари Python
                    '''

    if type(data) is str:
        data_file = os.path.split(data)[-1]
        data_type = data_file.split('.')[-1].lower()
    
        if data_type in ['yml', 'yaml']:
            vars_dict = yaml.load(open(data))
        elif data_type == 'json':
            vars_dict = json.load(open(data))
        else:
            print(error_message)
            return None
    elif type(data) is dict:
        vars_dict = data
    else:
        print(error_message)
        return None
    
    return template.render(vars_dict)

if __name__ == '__main__':
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
    
    
    print(generate_cfg_from_template(template_path, 'data_files\\for.yml'))
    print('\n\n')
    print(generate_cfg_from_template(template_path, 'data_files\\for.json'))
    print('\n\n')
    print(generate_cfg_from_template(template_path, data_dict))

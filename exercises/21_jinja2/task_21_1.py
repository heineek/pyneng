# -*- coding: utf-8 -*-
'''
Задание 21.1

Переделать скрипт cfg_gen.py в функцию generate_cfg_from_template.

Функция ожидает два аргумента:
* путь к шаблону
* файл с переменными в формате YAML

Функция должна возвращать конфигурацию, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных data_files/for.yml.

'''

from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os


template_path = sys.argv[1]
vars = sys.argv[2]


def generate_cfg_from_template(template_path, vars):
    template_dir, template_file = os.path.split(template_path)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True)
    template = env.get_template(template_file)
    
    vars_dict = yaml.load(open(vars))
    
    return template.render(vars_dict)

print(generate_cfg_from_template(template_path, vars))

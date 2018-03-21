# -*- coding: utf-8 -*-
'''
Задание 21.1a

Дополнить функцию generate_cfg_from_template из задания 21.1:

Функция generate_cfg_from_template должна принимать любые аргументы,
которые принимает класс Environment и просто передавать их ему.

То есть, надо добавить возможность контролировать аргументы trim_blocks, lstrip_blocks
и любые другие аргументы Environment через функцию generate_cfg_from_template.

Проверить функциональность на аргументах:
* trim_blocks
* lstrip_blocks

'''
from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os


template_path = sys.argv[1]
vars = sys.argv[2]


def generate_cfg_from_template(template_path, vars, trim_blocks=True,
                               lstrip_blocks=True):
    template_dir, template_file = os.path.split(template_path)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=trim_blocks,
        lstrip_blocks=lstrip_blocks)
    template = env.get_template(template_file)
    
    vars_dict = yaml.load(open(vars))
    
    return template.render(vars_dict)

print(generate_cfg_from_template(template_path, vars, trim_blocks=False,
                                 lstrip_blocks=False))

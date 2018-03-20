# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore=ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)


def config_to_dict(config):
    result = {}
    with open(config, 'r') as f:
        for line in f:
            if not line.strip() or line.startswith('!') or check_ignore(line):
                continue
            if not line.startswith(' '):
                curr_key = line.strip()
                result[curr_key] = []
            elif line.startswith(' ') and not line.startswith('  '):
                second_level_key = line
                result[curr_key].append(line.strip())
            else:
                if result[curr_key]:
                    result[curr_key] = {result[curr_key][0]: line}

    return(result)

print(config_to_dict('config_r1.txt'))

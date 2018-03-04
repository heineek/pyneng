# -*- coding: utf-8 -*-
"""
Задание 18.1

create_db.py
* сюда должна быть вынесена функциональность по созданию БД:
 * должна выполняться проверка наличия файла БД
 * если файла нет, согласно описанию схемы БД в файле dhcp_snooping_schema.sql,
   должна быть создана БД (БД отличается от примера в разделе)

В БД теперь две таблицы (схема описана в файле dhcp_snooping_schema.sql):
 * switches - в ней находятся данные о коммутаторах
 * dhcp - эта таблица осталась такой же как в примере, за исключением поля switch
  * это поле ссылается на поле hostname в таблице switches

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
"""
import os
import sqlite3

def create_db():
    db_filename = 'dhcp_snooping.db'
    schema_filename = 'dhcp_snooping_schema.sql'

    db_exists = os.path.exists(db_filename)
    if not db_exists:
        con = sqlite3.connect(db_filename)
        with con:
            with open(schema_filename, 'r') as f:
                schema = f.read()
                con.executescript(schema)
    else:
        print('Database already exists.')

if __name__ == '__main__':
    create_db()

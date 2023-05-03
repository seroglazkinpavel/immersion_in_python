'''Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.'''

import json
import csv


def get_ids(filename) -> set:
    file = open(filename, 'r', encoding='utf-8')
    all_ids = set()
    try:
        data = json.load(file)
        #csv_file = csv.reader(file)
        for level in data:
            for uid in level:
                all_ids.add(uid)
    except:
        pass
    file.close()
    return all_ids

def dump_json(wd, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(wd, file)


def get_data(all_ids: set, filename):
    working_dict: dict[int: dict[int: str]] = {}
    while True:
        name = input('Введите имя: ')
        if name == '':
            break
        user_id = -1
        while user_id < 0 or user_id in all_ids:
            user_id = int(input('Введите идентификатор: '))
        all_ids.add(user_id)
        access_level = 0
        while not 1 <= access_level <= 7:
            access_level = int(input('Введите уровень допуска (1 - 7): '))
        if working_dict.get(access_level):
            working_dict.get(access_level).update({user_id: name})
        else:
            working_dict[access_level] = {user_id: name}
        dump_json(working_dict, filename)


def func():
    all_ids = get_ids(filename)
    get_data(all_ids, filename)


'''Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV'''

def get_ids_csv(filename) -> set:
    file = open(filename, 'w', encoding='utf-8')
    all_ids = set()
    try:
        data = csv.reader(file)
        for level in data:
            for uid in level:
                all_ids.add(uid)
    except:
        pass
    file.close()
    return all_ids

def writer_csv_file(created_dist: dict, csv_file: str) -> None:
    rows = []
    for level, value in created_dist.items():
        for id, name in value.items():
            rows.append({'level': level, 'user_id': id, 'name': name})

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['level', 'user_id', 'name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def get_data_csv(all_ids: set, filename):
    working_dict: dict[int: dict[int: str]] ={}
    while True:
        name = input('Введите имя: ')
        if name == '':
            break
        user_id = -1
        while user_id < 0 or user_id in all_ids:
            user_id = int(input('Введите идентификатор: '))
        all_ids.add(user_id)
        access_level = 0
        while not 1 <= access_level <= 7:
            access_level = int(input('Введите уровень допуска (1 - 7): '))
        if working_dict.get(access_level):
            working_dict.get(access_level).update({user_id: name})
        else:
            working_dict[access_level] = {user_id: name}
        writer_csv_file(working_dict, filename)


def func_csv():
    all_ids = get_ids_csv('../csv_test.csv')
    get_data_csv(all_ids, '../csv_test.csv')


if __name__ == '__main__':
    func_csv()


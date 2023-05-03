'''Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов'''

import os
import json
import csv

def get_dir_size_old(path='.'):
    total = 0
    for p in os.listdir(path):
        full_path = os.path.join(path, p)
        if os.path.isfile(full_path):
            total += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total += get_dir_size_old(full_path)
    return total

def get_size_old(path='.'):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size_old(path)


def dictionary_creation(road: str):
    my_dct = {}
    for item in os.listdir(road):
        created_path = os.path.join(road, item)
        if os.path.isfile(created_path):
            parent = created_path.split('\\')[-2]
            object_type = 'File'
            object_size = get_size_old(created_path)
        elif os.path.isdir(created_path):
            parent = created_path.split('\\')[-2]
            object_type = 'Directory'
            get_size_old(os.path.join(road, item))
            object_size = get_size_old(created_path)
        #print(f'name -> {item} | object_type -> {object_type} | parent -> {parent} | number_of_bytes -> {object_size} | {created_path}')
        my_dct.setdefault(created_path, {'object_type':object_type, 'name': item, 'parent':parent, 'number_of_bytes': object_size})
    return my_dct


def writer_json_file(created_dist: dict, json_file: str) -> None:
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(created_dist, f, indent=4)

def writer_csv_file(created_dist: dict, csv_file: str) -> None:
    column = [['created_path', 'object_type',  'name', 'parent', 'number_of_bytes', ]]
    for key, val in created_dist.items():
        column.append([key, *val.values()])
    with open(csv_file, 'w', encoding='utf-8') as f:
        write_csv = csv.writer(f, dialect='excel', delimiter=';')
        write_csv.writerows(column)



def main(road: str, json_file: str, csv_file: str):
    my_dict = dictionary_creation(road)
    writer_json_file(my_dict, json_file)
    writer_csv_file(my_dict, csv_file)

if __name__ == '__main__':
    main( r'C:\test\test1', '../json_file.json', 'csv_file.csv')


'''Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.'''

import random
import csv
import json
import math
import os.path
from typing import Callable


def decor_csv(func: Callable):
    csv_file_generation()
    def wrapper():
        with open('random_name.csv', 'r', encoding='utf-8', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                args = (int(j) for j in row)
                print(func(*args))
    return wrapper


def save_to_json(func):
    file = Path(f"{func.__name__}.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
    else:
        json_file = []
    def wrapper(*args, **kwargs):
        for result in func(*args, **kwargs):
            if result:
                dct = {'args': args, **kwargs, 'result': str(result)}
                json_file.append(dct)
                with open(file, 'w', encoding='utf-8') as json_f:
                    json.dump(json_file, json_f, indent=2)
            else:
                break
    return wrapper


def decor_json(func: Callable):
    file_name = os.path.join(os.getcwd(), f'{func.__name__}.json')
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
    else:
        json_file = []
    def wrapper(*args):
        result = func(*args)
        dump_dict = {}
        dump_dict['arguments'] = [*args]
        dump_dict['result'] = [*result]
        json_file.append(dump_dict)
        with open(file_name, 'w', encoding='utf-8') as json_f:
            json.dump(json_file, json_f, indent=2)
    return wrapper


def csv_file_generation():
    list_rows = []
    for _ in range(100, 1000):
        a, b, c = random.sample(range(-1000, 1000), 3)
        list_rows.append({'a': a, 'b': b, 'c': c})
    with open('random_name.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['a', 'b', 'c']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_rows)

#@decor_json
@decor_csv
def finding_roots(*args):
    a, b, c = args
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x

if __name__ == '__main__':
    print(finding_roots())
    #finding_roots(7, 2, -8)

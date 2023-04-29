'''Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.'''

from random import randint, uniform

def fills_file(quantity: int, name_file: str):
    with open(name_file, 'w', encoding='utf-8') as f:
        for i in range(quantity):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num: >5} | {float_num: .3f}\n')


if __name__ == '__main__':
    fills_file(20, 'my_file')
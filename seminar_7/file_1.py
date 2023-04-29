'''Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.'''


import os
from pathlib import Path

def renaming_files(number_of_digits: int, source_file_extension: str,
                   destination_file_extension: str, range_name: list[int], new_name: str=''):
    count = 0
    for file in os.listdir():
        extension = file.split('.')
        old_file = extension[0][range_name[0]:range_name[1]]
        if len(extension) > 1 and extension[1].lower() == source_file_extension:
            count += 1
            Path(file).rename(f"{old_file}{new_name}{count:0>{number_of_digits}}.{destination_file_extension}")

if __name__ == '__main__':
    renaming_files(3, 'php', 'txt', [0, 2], 'rem')

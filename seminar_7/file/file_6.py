'''Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.'''
import os
from pathlib import Path
from file_5 import get_files, my_dict

def create_dir(name_dir: str):
    name = Path(Path.cwd()/name_dir)
    if not name.exists():
        name.mkdir()
    os.chdir(name)
    get_files(my_dict)

if __name__ == '__main__':
    create_dir('other')

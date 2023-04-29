'''Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.'''
import os
import shutil
from pathlib import Path

source_folder = r'C:/Users/MSI/Desktop'  # исходная папка
folder_move = r'C:/Users/MSI/Desktop'  # папка куда будет переносится файлы
photoshop_files = ['pdf', 'psd', 'png', 'jpeg', 'psb']
video_files = ['dat', 'bin', 'drv', 'flv', 'f4v', 'avi']
text_files = ['txt', 'text', 'log', 'sub', 'pwi']


def file_sorting():
    files = os.listdir(source_folder)
    for items in files:
        extension = items.split('.')
        if len(extension) > 1 and extension[1].lower() in photoshop_files:
            old_file = source_folder + '/' + items
            new_path = folder_move + '/PHOTOSHOP/' + items
            shutil.move(old_file, new_path)
        elif len(extension) > 1 and extension[1].lower() in video_files:
            old_file = source_folder + '/' + items
            new_path = folder_move + '/VIDEO/' + items
            shutil.move(old_file, new_path)
        elif len(extension) > 1 and extension[1].lower() in text_files:
            old_file = source_folder + '/' + items
            new_path = folder_move + '/TEXT/' + items
            shutil.move(old_file, new_path)


if __name__ == '__main__':
    file_sorting()
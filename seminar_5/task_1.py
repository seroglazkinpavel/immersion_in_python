'''Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.'''

link = 'C:/Users/MSI/Desktop/python_test/seminar_4/task.py'

def returns_a_tuple(link: str) -> tuple[str]:
    *prefix, suffix = link.split('/')
    file_name, file_extension = suffix.split('.')
    my_list = []
    my_list.append('/'.join(prefix))
    my_list.append(file_name)
    my_list.append(file_extension)
    return tuple(my_list)
print(returns_a_tuple(link))


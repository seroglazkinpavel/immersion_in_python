'''Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.'''
import csv
from functools import reduce
from pathlib import Path
from check import Check

class Student:
    name = Check()
    second_name = Check()
    surname = Check()
    _subjects = None

    def __init__(self, name: str, second_name: str, surname: str, subjects: Path):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.subjects = subjects

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, list_of_items: Path):
        if self.subjects is not None:
            raise AttributeError(f'Список предметов уже есть')
        self._subjects = []
        with open(list_of_items, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self._subjects.append(row)
        for i in range(len(self._subjects)):
            self._subjects[i]['estimation'] = []
            self._subjects[i]['test'] = []


    def data_storage(self, item_name: str, subject_grade: int, test_results: float):
        if item_name not in [self.subjects[i].get('subject')for i in range(len(self.subjects))]:
            raise ValueError("Нет такого предмета.")

        if subject_grade < 2 or subject_grade > 5:
            raise ValueError("Оценка вне диапазона 2-5")

        if test_results < 0 or test_results > 100:
            raise ValueError("Результаты теста вне диапазона 0-100")
        for i in range(len(self.subjects)):
            if self.subjects[i]['subject'] == item_name:
                self.subjects[i]['estimation'].append(subject_grade)
                self.subjects[i]['test'].append(test_results)

        return self.subjects

    def average_score_on_tests(self):
        my_list = []
        for i in self.subjects:
            if len(i['test']) != 0:
                my_list.append(sum(i['test'])) / len(i['test'])
            else:
                my_list.append(0)
        return my_list

    def average_estimate_of_subjects(self):
        my_list = []
        for i in self.subjects:
            my_list.extend(i['estimation'])
        return sum(my_list)/len(my_list)

    def __repr__(self):
        result = f'''Студент фио"{self.name} {self.second_name} {self.surname}", средний балл по предметам={self.average_estimate_of_subjects()}\n'''
        for name in self.subjects:
            result += f'{name}\n'

        return result

if __name__ == '__main__':
    student = Student("Mikhail", "Sergeevich", "Fedko", Path('subjects.csv'))
    print(student.subjects)
    student.data_storage('physics', 3, 50)
    student.data_storage('physics', 3, 70)
    student.data_storage('physics', 5, 60)
    student.data_storage('mathematics', 5, 70)
    student.data_storage('physics', 4, 99)
    student.data_storage('story', 2, 79)
    student.data_storage('story', 3, 55)
    student.data_storage('story', 5, 9)
    student.data_storage('story', 4, 15)
    student.data_storage('biology', 2, 79)
    student.data_storage('biology', 3, 55)
    student.data_storage('biology', 5, 9)
    student.data_storage('biology', 4, 15)
    print(student.average_score_on_tests())
    print(student)
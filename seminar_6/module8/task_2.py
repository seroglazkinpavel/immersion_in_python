'''Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.'''

from random import randint

n = 8
x = [0] * n
y = [0] * n
result = 'True'
for i in range(n):
    x[i], y[i] = [int(j) for j in input('Введите числа через пробел: ').split()]
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            result = 'False'

'''Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и
выведите 4 успешных расстановки.'''


def arrangement():
    n = 8
    x = [0] * n
    y = [0] * n
    list1 = []
    while len(list1) != 4:
        result = 'True'
        for i in range(n):
            x[i], y[i] = [int(j) for j in [randint(1, 8), randint(1, 8)]]
        for i in range(n):
            for j in range(i + 1, n):
                if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    result = 'False'
        if result == 'True':
            my_list = list(zip(x, y))
            list1.append(set(my_list))

    return list1


if __name__ == '__main__':
    print(result)
    #print(arrangement())

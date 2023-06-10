'''Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.'''

'''Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, 
равнобедренным или равносторонним.'''

import argparse
from triangle_exception import TriangleMinLengthError, TriangleError

def triangle(a: int, b: int, c: int):
    if a < 0:
        raise TriangleMinLengthError(a, 0)
    if b < 0:
        raise TriangleMinLengthError(b, 0)
    if c < 0:
        raise TriangleMinLengthError(c, 0)
    check1 = a + b
    check2 = a + c
    check3 = b + c
    if (check1 < c or check2 < b or check3 < a):
        raise TriangleError(a, b, c)
    else:
        if (a == b and b == c and c == a):
            print("Треугольник равносторонний")
        elif a == b or b == c or c == a:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Получаем треугольник')
    parser.add_argument('-a', type=int, default=3)
    parser.add_argument('-b', type=int, default=2)
    parser.add_argument('-c', type=int, default=4)

    args = parser.parse_args()


    triangle(args.a, args.b, args.c)

    # python ./seminar_15/triangle_1.py -a=4 -b=2 -c=2
    # python ./seminar_15/triangle_1.py -a=4 -b=4 -c=4
    # python ./seminar_15/triangle_1.py
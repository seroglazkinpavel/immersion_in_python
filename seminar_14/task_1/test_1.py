'''Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним тесты.
2-5 тестов на задачу в трёх вариантах:
○ doctest,
○ unittest,
○ pytest.'''

'''напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.'''
from cmath import sqrt


def quadratic_equations(a: complex, b: complex, c: complex):
    """
    Решает квадратные уравнения даже если дискриминант отрицательный.
    >>> quadratic_equations(2, 7, 5)
    (9, (-1+0j), (-2.5+0j))
    >>> quadratic_equations(6, 3, 7)
    (-159, (-0.25+1.050793351076541j), (-0.25-1.050793351076541j))
    """
    discr: complex = b * b - 4 * a * c
    x1: complex = (-b + sqrt(discr)) / (2 * a)
    x2: complex = (-b - sqrt(discr)) / (2 * a)
    return discr, x1, x2


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

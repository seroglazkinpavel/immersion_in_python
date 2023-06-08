'''напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.'''
import pytest
from cmath import sqrt


def quadratic_equations(a: complex, b: complex, c: complex):
    """
    Решает квадратные уравнения даже если дискриминант отрицательный.
    """
    discr: complex = b * b - 4 * a * c
    x1: complex = (-b + sqrt(discr)) / (2 * a)
    x2: complex = (-b - sqrt(discr)) / (2 * a)
    return discr, x1, x2


def test():
    assert quadratic_equations(2, 7, 5) == (9, (-1 + 0j), (-2.5 + 0j)), 'Ошибка тест 1'
    assert quadratic_equations(6, 3, 7) == (
    -159, (-0.25 + 1.050793351076541j), (-0.25 - 1.050793351076541j)), 'Ошибка тест 2'


if __name__ == '__main__':
    pytest.main(['-v'])

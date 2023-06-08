'''напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.'''
from cmath import sqrt
import unittest


def quadratic_equations(a: complex, b: complex, c: complex):
    """
    Решает квадратные уравнения даже если дискриминант отрицательный.
    """
    discr: complex = b * b - 4 * a * c
    x1: complex = (-b + sqrt(discr)) / (2 * a)
    x2: complex = (-b - sqrt(discr)) / (2 * a)
    return discr, x1, x2


class TestCaseName(unittest.TestCase):
    def test_metod(self):
        self.assertEqual(quadratic_equations(2, 7, 5), (9, (-1+0j), (-2.5+0j)))
        self.assertEqual(quadratic_equations(6, 3, 7), (-159, (-0.25+1.050793351076541j), (-0.25-1.050793351076541j)))


if __name__ == '__main__':
    unittest.main(verbosity=2)


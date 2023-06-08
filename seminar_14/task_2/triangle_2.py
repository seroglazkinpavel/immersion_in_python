import unittest
from seminar_14.task_2.triangle import Triangle

class TestCaseName(unittest.TestCase):
    def test_metod(self):
        self.assertEqual(Triangle(2, 2, 2).type, 'Равносторонний')
        self.assertEqual(Triangle(1, 2, 2).type, 'Равнобедренный')
        self.assertEqual(Triangle(1, 2, 3).type, 'Разносторонний')


if __name__ == '__main__':
    unittest.main(verbosity=2)
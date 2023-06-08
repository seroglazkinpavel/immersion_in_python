import pytest
from seminar_14.task_2.triangle import Triangle


def test():
    assert Triangle(2, 2, 2).type == 'Равносторонний', 'Ошибка тест 1'
    assert Triangle(1, 2, 2).type == 'Равнобедренный', 'Ошибка тест 2'
    assert Triangle(1, 2, 3).type == 'Разносторонний', 'Ошибка тест 2'


if __name__ == '__main__':
    pytest.main(['-v'])

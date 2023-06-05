'''Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.'''

'''Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.'''

'''Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.'''

from rectangle_exception import RectangleLengthError


class Rectangle:

    def __init__(self, side_a: float, side_b: float):
        if side_a > 0:
            self._side_a = side_a
        else:
            raise RectangleLengthError(a, 0)
        if side_b > 0:
            self._side_b = side_b
        else:
            raise RectangleLengthError(b, 0)

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)

    def get_area(self):
        return self._side_a * self._side_b

    def __add__(self, other):
        ratio = self._side_a / self._side_b
        perimeter = self.get_perimeter() + other.get_perimeter()
        return Rectangle((perimeter / 2) * ratio, (perimeter / 2) - (perimeter / 2) * ratio)

    def __sub__(self, other):
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self._side_a}, {self._side_b} и периметром {self.get_perimeter()}"


if __name__ == '__main__':
    TEXT = f"Введите длинну стороны прямоугольника: "
    try:
        a = int(input(TEXT + "№1: "))
        b = int(input(TEXT + "№2: "))
        rectangle = Rectangle(a, b)
    except ValueError as e:
        print(f"Нужно задать число: {e}")

    print(f'{rectangle.get_perimeter() = :2f}, {rectangle.get_area() = :2f}')
    rect1 = Rectangle(1, 5)
    rect2 = Rectangle(2, 4)
    rect3 = rect1 + rect2
    print(rect3)

    rect4 = Rectangle(1, 5)
    rect5 = Rectangle(2, 7)
    rect6 = rect4 + rect5
    print(rect6)

    print(rect1 < rect2)
    print(rect1 > rect2)
    print(rect1 <= rect2)
    print(rect1 >= rect2)
    print(rect1 == rect2)
    print(rect1 != rect2)

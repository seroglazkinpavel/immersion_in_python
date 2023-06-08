'''Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.'''

class Triangle:

    def __init__(self, a: float, b: float, c: float):

        if Triangle.validate(a, b, c):
            self.a: float = a
            self.b: float = b
            self.c: float = c
            self.__type = None
        else:
            print("Такого треугольника не существует")

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, number: float):
        self._a = number

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, number: float):
        self._b = number

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, number: float):
        self._c = number

    @staticmethod
    def validate(*args, flag: bool = True):
        for i in args:
            if sum(args) - i < i:
                flag = False
                break
        return flag

    def __str__(self):
        return f"Треугольник со сторонами {self.a}, {self.b}, {self.c}"

    @property
    def type(self):
        if self.__type is None:
            count = 0
            for i in self.__dict__.values():
                temp = list(self.__dict__.values()).count(i)
                count = temp if count < temp else count
            self.__type = ["Разносторонний", "Равнобедренный", "Равносторонний"][count - 1]
        return self.__type

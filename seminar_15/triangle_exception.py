import logging

logging .basicConfig(
    filename='task01.log',
    filemode='a',
    encoding='utf-8',
    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
    style='{',
    level=logging.ERROR)
logger = logging.getLogger(__name__)
class TriangleExceptions(Exception):
    pass


class TriangleMinLengthError(TriangleExceptions):

    def __init__(self, param, value):
        self.param = param
        self.value = value

    def __str__(self):

        if self.param < self.value:
            logger.error(f'Сторона треугольника не может быть меньше нуля\n' \
                   f'Заданное число {self.param} < {self.value}')
            return f'Сторона треугольника не может быть меньше нуля\n' \
                   f'Заданное число {self.param} < {self.value}'
        elif self.param == self.value:
            logger.error(f'Сторона треугольника не может быть равна нулю\n' \
                   f'Заданное число {self.param} = {self.value}')
            return f'Сторона треугольника не может быть равна нулю\n' \
                   f'Заданное число {self.param} = {self.value}'


class TriangleError(TriangleExceptions):

    def __init__(self, value1: int, value2: int, value3: int):
        self.a = value1
        self.b = value2
        self.c = value3

    def __str__(self):
        logger.error(f"Tреугольника со сторонами {self.a}, {self.b}, {self.c} не существует!")
        print(f"Tреугольника со сторонами {self.a}, {self.b}, {self.c} не существует!")






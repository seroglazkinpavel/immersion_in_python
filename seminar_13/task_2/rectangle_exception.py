class RectangleExceptions(Exception):
    pass


class RectangleLengthError(RectangleExceptions):

    def __init__(self, param, value):
        self.param = param
        self.value = value

    def __str__(self):

        if self.param < self.value:
            return f'Сторона прямоугольника не может быть меньше нуля\n' \
                   f'Заданное число {self.param} < {self.value}'
        elif self.param == self.value:
            return f'Сторона прямоугольника не может быть равна нулю\n' \
                   f'Заданное число {self.param} = {self.value}'



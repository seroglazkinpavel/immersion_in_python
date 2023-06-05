class StudentException(Exception):
    pass


class StudentStrError(StudentException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value} должно быть строкой.'


class StudentLetterError(StudentException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if not self.value.isalpha():
            return f'В {self.value} должны быть только буквы.'
        elif not self.value.istitle():
            return f'В {self.value} первая буква должна быть заглавной.'


class StudentSubjectsError(StudentException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Нет такого предмета {self.value}.'


class StudentEstimateError(StudentException):
    def __init__(self, value, lower, upper):
        self.value = value
        self.lower = lower
        self.upper = upper

    def __str__(self):
        text = ''
        if self.value < self.lower:
            text = 'меньше нижней'
        elif self.value > self.lower:
            text = 'больше верхней'
        return f'Оценка {self.value} {text} границы. Попадите в диапазон ({self.lower}, {self.upper}).'
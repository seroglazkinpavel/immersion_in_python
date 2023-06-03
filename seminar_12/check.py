class Check:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'{value} должно быть строкой.')
        if not value.isalpha():
            raise ValueError(f'В {value} должны быть только буквы.')
        if not value.istitle():
            raise ValueError(f'В {value} первая буква должна быть заглавной.')

'''Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.'''


class Animal:
    def __init__(self, name: str, age: int):
        self.__name, self.__age = name, age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age


class Fish(Animal):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.__color = color

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


class Mammal(Animal):
    def __init__(self, name: str, age: int, wool: str):
        super().__init__(name, age)
        self.__wool = wool

    @property
    def wool(self) -> str:
        return self.__wool

    @wool.setter
    def wool(self, wool: str):
        self.__wool = wool


class Bird(Animal):
    def __init__(self, name: str, age: int, feather: str):
        super().__init__(name, age)
        self.__feather = feather

    @property
    def feather(self) -> str:
        return self.__feather

    @feather.setter
    def feather(self, feather: str):
        self.__feather = feather


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, *args):
        if animal_type == 'fish':
            return Fish(*args)
        elif animal_type == 'mammal':
            return Mammal(*args)
        elif animal_type == 'bird':
            return Bird(*args)
        else:
            raise ValueError('Неверный тип животного.')


if __name__ == '__main__':
    animalFactory = AnimalFactory()

    fish = animalFactory.create_animal('fish', 'Рыба-кит', 5, 'синий')
    print(f'name:{fish.name} age:{fish.age} color:{fish.color}')

    mammal = animalFactory.create_animal('mammal', 'медведь', 15, 'длинная')
    print(f'name:{mammal.name} age:{mammal.age} wool:{mammal.wool}')

    bird = animalFactory.create_animal('bird', 'синичка', 1, 'красивые')
    print(f'name:{bird.name} age:{bird.age} feather:{bird.feather}')

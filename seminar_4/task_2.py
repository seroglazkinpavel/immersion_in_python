'''Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.'''


def translation_to_dict(**kwargs) -> dict:
    my_dict = {}
    for key, value in kwargs.items():
        try:
            my_dict[value] = key
        except:
            my_dict[str(value)] = key
    return my_dict


print(translation_to_dict(day='Thursday', number=15, sun=True, spring=['тепло', 'зелень', 'нерест']))

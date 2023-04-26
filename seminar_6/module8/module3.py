'''Улучшаем задачу 2. Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.'''
from random import randint


def func(min_value, max_value, tries):
    num = randint(min_value, max_value)
    guess_num = 0
    count = 1
    while guess_num != num:
        if count > tries:
            print("К сожалению попытки закончились, вы проиграли")
            break
        print("Попытка № ", count)
        guess_num = int(input("Введите предполагаемое число: "))
        if guess_num > num:
            print("Введите число поменьше")
        elif guess_num == num:
            print("Вы угадали! Поздравляю!")
        else:
            print("Введите число побольше")
        count += 1


def puzzle(puzzle_text: str, solutions: list[str], tries: int) -> int:
    print(puzzle_text)
    solutions = list(map(lambda x: x.lower(), solutions))
    num = 0
    while num < tries:
        user_input = input('Введите вариант ответа: ').lower()
        if user_input in solutions:
            return num + 1
        else:
            print('Не угадал, попробуй еще.')
        num += 1
    return 0


def puzzle_solut():
    dict_puzzle = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'],
                   'Висит груша нельзя скушать': ['груша', 'игрушка', 'лампочка']}
    for key, value in dict_puzzle.items():
        puzzle(key, value, randint(1, 5))


_solutions = {}
puzzle_dict = {
    'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'],
    'Висит груша нельзя скушать': ['груша', 'игрушка', 'лампочка']
}


def puzzle_solver(puzzle_text: str, tries: int):
    num = puzzle(puzzle_text, puzzle_dict[puzzle_text], tries)
    _solutions[puzzle_text] = [num, True if num else False]


def show_results():
    for k, v, in _solutions.items():
        print(k, v)


if __name__ == '__main__':
    pass

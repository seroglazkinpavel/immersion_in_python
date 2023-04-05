'''Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 1

number = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
if number == num:
    print('Вы выграли, поздравляем!')
else:
    while True:
        if number == num:
            print('Вы выграли, поздравляем!')
            break
        elif number > num:
            print('Много, попробуете еще раз!')
            number = int(input('Введите еще раз число: '))
        elif number < num:
            print('Мало, попробуете еще раз!')
            number = int(input('Введите еще раз число: '))
        count += 1
        if count == 10:
            print('Лимит закончился')
            break
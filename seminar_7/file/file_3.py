'''✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.'''

from random import randint, uniform

def write_random(filename: str, count_lines: int) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(count_lines):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num:>5} | {float_num:.3f}\n')



def whatever():
    with (open('my_file', 'r', encoding='utf-8') as fnumbers,
          open('names.txt', 'r', encoding='utf-8') as fnames):
        numbers = fnumbers.readlines()
        names = fnames.readlines()
    lines_to_write = []
    length_of_longest = max(len(numbers), len(names))
    for i in range(length_of_longest):
        two_numbers = numbers[i % len(numbers)]
        a, b = map(float, two_numbers.split('|'))
        mult = a * b
        name = names[i % len(names)]
        if mult >= 0:
            lines_to_write.append(f'{name.upper().rstrip()}; {round(mult)}\n')
        else:
            lines_to_write.append(f'{name.lower().rstrip()}; {abs(mult)}\n')
    with open('endfile.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines_to_write)

if __name__ == '__main__':
    whatever()
    write_random('my_file', 20)
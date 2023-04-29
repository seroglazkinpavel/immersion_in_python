'''Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.'''

from random import randint, choices

VOWELS = 'aeияюзыуоё'
CONSONANTS = ''.join([chr(ch) for ch in range(ord("а"), ord("я") + 1) if chr(ch) not in VOWELS])

def make_random_name(amount_of_names: int):
    count = 0
    all_name = []
    while count != amount_of_names:
        word_len = randint(4, 7)
        word = choices(VOWELS + CONSONANTS, k=word_len)
        if any(ch in VOWELS for ch in word):
            all_name.append(''.join(word).capitalize() + '\n')
            count += 1
    with open('names.txt', 'w', encoding='utf-8') as f:
        f.writelines(all_name)


if __name__ == '__main__':
    make_random_name(10)
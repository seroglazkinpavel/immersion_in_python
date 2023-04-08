'''Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.'''
#Функция chr() преобразует число в символ Юникода, обратная операция ord().
'''def hex_number(number: int, mod: int = 16) -> str:
    result = ''
    while number != 0:
        temp = number % mod if (number % mod) < 10 else chr(number % mod + 87)
        result = str(temp) + result
        number //= mod
    result = "0x" + result
    return result
print(hex_number(588, 16)) #0x24c'''
num = int(input('Введите число: '))
print(hex(num))
str_rep = ''
while num:
    if num % 16 < 10:
        temp = num % 16
    else:
        temp = chr(num % 16 + 87)
    str_rep = str(temp) + str_rep
    num //= 16

print(str_rep)



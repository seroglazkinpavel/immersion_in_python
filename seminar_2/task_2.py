'''Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.'''

import fractions
import math

text1: str = input("Введите дробь вида a/b: ")
text2: str = input("Введите вторую дробь вида c/d: ")
result: str = ""
result2: str = ""
numerator: int = 0    # числитель
denominator: int = 0  # знаменатель
a: str = ""
b: str = ""
c: str = ""
d: str = ""
# Определяем abcd
for item in text1:
    if item != "/":
        a += item
    else:
        break
for item in text1[::-1]:
    if item != "/":
        b = item + b
    else:
        break
for item in text2:
    if item != "/":
        c += item
    else:
        break
for item in text2[::-1]:
    if item != "/":
        d = item + d
    else:
        break

a: int = int(a)
b: int = int(b)
c: int = int(c)
d: int = int(d)

# Определяем сумму дробей

if b == d:
    temp1: int = a + c
    temp2: int = b
    """Наибольший общий делитель двух чисел"""
    nod = math.gcd(temp1, temp2)
    """определение числителя и знаменателя"""
    numerator = temp1 // nod
    denominator = temp2 // nod
    result = f"{numerator}/{denominator}"
    if numerator % denominator == 0:
        result = str(numerator // denominator)
else:
    temp1 = a * d
    temp2 = c * b
    """Наибольший общий делитель двух чисел"""
    nod = math.gcd(temp1, temp2)
    """определение числителя и знаменателя"""
    numerator = (temp1 + temp2) // nod
    denominator = (b * d) // nod
    result = f"{numerator}/{denominator}"

print(f"Результат суммы {result}")

"""Проверка с fractions"""
f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)
print(f"Проверка решения суммы с помощью модуля fractions {f1 + f2}")

# Умножение дробей

temp1 = a * c
temp2 = b * d
"""Наибольший общий делитель двух чисел"""
nod = math.gcd(temp1, temp2)
"""определение числителя и знаменателя"""
numerator = temp1 // nod
denominator = temp2 // nod
if numerator % denominator == 0:
    result2 = str(numerator // denominator)
else:
    result2 = f"{numerator}/{denominator}"

print(f"Умножение {result2}")
"""Проверка с fractions"""
print(f"Проверка решения умножения с помощью модуля fractions {f1 * f2}")
# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fib_gen():
    yield 0
    a = 1
    b = 1
    while True:
        yield b
        a, b = b, a+b

g = fib_gen()

for i in range(20):
    print(next(g))



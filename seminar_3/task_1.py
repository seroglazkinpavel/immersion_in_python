'''Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.'''


from random import random

data = []
for i in range(10):
    data.append(int(random() * 10))
print(f'Данный список {data}')

# Решение с помощью функции: фильтра filter и анонимной lambda
#print(list(set(filter(lambda x: data.count(x) > 1, data))))

my_list = []
for item in data:
    if data.count(item) > 1:
        my_list.append(item)
print(f'Список с дублирующими элементами {my_list}')

print(f'Результирующий список без дубликатов {set(my_list)}')

'''В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.'''

text = "И вечный бой! Покой нам только снится Сквозь кровь и пыль… Летит, летит степная кобылица И мнет ковыль… \
        И нет конца! Мелькают версты, кручи… Останови! Идут, идут испуганные тучи, Закат в крови! Закат в крови! \
        Из сердца кровь струится! Плачь, сердце, плачь… Покоя нет! Степная кобылица Несется вскачь! А.А. Блок"

import string

print(text)

delete = string.punctuation
#delete = ',.'
for i in delete:
    text = (text.replace(i, "")).lower()
text = text.split()
print(text)

my_dict = {}

for world in text:
    my_dict[world] = text.count(world)

my_values = sorted(my_dict.values(), reverse=True)
my_keys = my_dict.keys()
my_count = 10
dict_result ={}
for value in my_values:
    for key in my_keys:
        if my_dict[key] == value and key not in dict_result:
            dict_result[key] = my_dict[key]
            my_count -= 1
            break
    if my_count <= 0:
        break
print(dict_result)
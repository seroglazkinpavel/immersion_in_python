'''Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии '''

names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = ['10.0%', '7.25%', '13.5%']

my_dict = {name: salary + salary * float(award[:-1])/100 for name, salary, award in zip(names, salaries, awards)}

print(my_dict)
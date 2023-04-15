'''Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.'''

'''Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег'''

operation = []
bank = 0
count = 0
def add_bank(cash: int):
    global bank, count, operation
    bank += cash
    count += 1
    operation.append(f'Добавлено: {cash}')

def take_bank(cash: int) ->None:
    global bank, count, operation
    if cash <= 2000: # Если 30 это 1.5%, то 100% это 2000
        cash -= 30
    elif 2001 <= cash <= 40000: # Если 600 это 1.5%, то 100% это 40000
        cash *= 0.985           # комисия 1.5% значит умножаем на 0.985
    else:
        cash -= 600
    bank -= cash
    count += 1
    operation.append(f'Снято: {cash}')

def exit_bank():
    print('Рады видеть вас снова!')
    exit()

def check_bank() ->int:
    while True:
        cash = int(input('Введите сумму операции кратную 50: '))
        if cash % 50 == 0:
            return cash
def main():
    while True:
        global bank, count

        action = input('1 - снять\n2 - пополнить\n3 - выйти:\n')
        if bank >= 5_000_000:
            bank *= 0.9
        match action:
            case '1':
                cash = check_bank()
                if cash < bank:
                    take_bank(cash)
                else:
                    print('Нет денег!')
            case '2':
                add_bank(check_bank())
            case '3':
                exit_bank()
        if count == 3:
            bank *= 1.03
            count = 0
        print('Ваш баланс: ', bank)
        print('Операции:', operation)



print(main())
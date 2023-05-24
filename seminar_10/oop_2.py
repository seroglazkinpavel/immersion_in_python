'''Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег'''


class CashMachine:
    def __init__(self, operation: list=[], bank: float=0, count: int=0, cash: int=0):
        self.__operation = operation
        self.__bank = bank
        self.__count = count
        self.cash = cash

    def add_bank(self, cash: int):
        #global bank, count, operation
        self.__bank += self.cash
        self.__count += 1
        self.__operation.append(f'Добавлено: {self.cash}')

    def take_bank(self, cash: int) -> None:
        #global bank, count, operation
        if self.cash <= 2000:  # Если 30 это 1.5%, то 100% это 2000
            self.cash -= 30
        elif 2001 <= self.cash <= 40000:  # Если 600 это 1.5%, то 100% это 40000
            self.cash *= 0.985  # комисия 1.5% значит умножаем на 0.985
        else:
            cash -= 600
        self.__bank -= self.cash
        self.__count += 1
        self.__operation.append(f'Снято: {self.cash}')

    def exit_bank(self):
        print('Рады видеть вас снова!')
        exit()

    def check_bank(self) -> int:
        while True:
            self.cash = int(input('Введите сумму операции кратную 50: '))
            if self.cash % 50 == 0:
                return self.cash

    def main(self):
        while True:
            #global bank, count

            action = input('1 - снять\n2 - пополнить\n3 - выйти:\n')
            if self.__bank >= 5_000_000:
                self.__bank *= 0.9
            match action:
                case '1':
                    self.cash = self.check_bank()
                    if self.cash < self.__bank:
                        self.take_bank(self.cash)
                    else:
                        print('Нет денег!')
                case '2':
                    self.add_bank(self.check_bank())
                case '3':
                    self.exit_bank()
            if self.__count == 3:
                self.__bank *= 1.03
                self.__count = 0
            print('Ваш баланс: ', self.__bank)
            print('Операции:', self.__operation)


if __name__ == "__main__":
    cashMachine = CashMachine()
    cashMachine.main()
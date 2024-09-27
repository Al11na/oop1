class Money:
    def __init__(self, rubles=0, kopecks=0):
        self.rubles = rubles
        self.kopecks = kopecks
        self._normalize()

    def _normalize(self):
        """Приводим значение копеек к нормальной форме."""
        if self.kopecks >= 100:
            self.rubles += self.kopecks // 100
            self.kopecks = self.kopecks % 100
        elif self.kopecks < 0:
            self.rubles -= (-self.kopecks) // 100 + 1
            self.kopecks = 100 - (-self.kopecks) % 100

    def read(self):
        """Ввод значения с клавиатуры."""
        self.rubles = int(input("Введите количество рублей: "))
        self.kopecks = int(input("Введите количество копеек: "))
        self._normalize()

    def display(self):
        """Вывод значения на экран."""
        print(f"{self.rubles},{self.kopecks:02d} руб.")

    def __add__(self, other):
        """Сложение денежных сумм."""
        new_rubles = self.rubles + other.rubles
        new_kopecks = self.kopecks + other.kopecks
        return Money(new_rubles, new_kopecks)

    def __sub__(self, other):
        """Вычитание денежных сумм."""
        new_rubles = self.rubles - other.rubles
        new_kopecks = self.kopecks - other.kopecks
        return Money(new_rubles, new_kopecks)

    def __mul__(self, factor):
        """Умножение суммы на дробное число."""
        total_kopecks = (self.rubles * 100 + self.kopecks) * factor
        new_rubles = int(total_kopecks // 100)
        new_kopecks = int(total_kopecks % 100)
        return Money(new_rubles, new_kopecks)

    def __truediv__(self, divisor):
        """Деление суммы на дробное число."""
        total_kopecks = (self.rubles * 100 + self.kopecks) / divisor
        new_rubles = int(total_kopecks // 100)
        new_kopecks = int(total_kopecks % 100)
        return Money(new_rubles, new_kopecks)

    def __eq__(self, other):
        """Сравнение двух сумм на равенство."""
        return self.rubles == other.rubles and self.kopecks == other.kopecks

    def __lt__(self, other):
        """Операция меньше."""
        return (self.rubles, self.kopecks) < (other.rubles, other.kopecks)

    def __le__(self, other):
        """Операция меньше или равно."""
        return (self.rubles, self.kopecks) <= (other.rubles, other.kopecks)


if __name__ == '__main__':
    # Демонстрация работы класса Money
    m1 = Money()
    m2 = Money()

    print("Введите первую денежную сумму:")
    m1.read()

    print("Введите вторую денежную сумму:")
    m2.read()

    print("Первая сумма:")
    m1.display()

    print("Вторая сумма:")
    m2.display()

    # Сложение и вычитание сумм
    sum_money = m1 + m2
    print("Сумма двух денежных сумм:")
    sum_money.display()

    sub_money = m1 - m2
    print("Разность двух денежных сумм:")
    sub_money.display()

    # Умножение на число
    factor = float(input("Введите число, на которое хотите умножить первую сумму: "))
    mul_money = m1 * factor
    print(f"Умножение первой суммы на {factor}:")
    mul_money.display()

    # Деление на число
    divisor = float(input("Введите число, на которое хотите разделить первую сумму: "))
    div_money = m1 / divisor
    print(f"Деление первой суммы на {divisor}:")
    div_money.display()

    # Операции сравнения
    print("Первая сумма равна второй?", m1 == m2)
    print("Первая сумма меньше второй?", m1 < m2)

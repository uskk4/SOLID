from abc import ABC, abstractmethod

class Discount(ABC):
    """
    Базовий клас для розрахунку знижок.
    """
    @abstractmethod
    def calculate(self, price):
        pass


class NoDiscount(Discount):
    """
    Клас для відсутності знижки.
    """
    def calculate(self, price):
        return price


class PercentageDiscount(Discount):
    """
    Клас для знижки у відсотках.
    """
    def __init__(self, percentage):
        self.percentage = percentage

    def calculate(self, price):
        return price * (1 - self.percentage / 100)


class FixedAmountDiscount(Discount):
    """
    Клас для фіксованої знижки.
    """
    def __init__(self, amount):
        self.amount = amount

    def calculate(self, price):
        return max(0, price - self.amount)


# Використання
def apply_discount(price, discount):
    """
    Функція для застосування знижки до ціни.
    """
    return discount.calculate(price)


# Ціна продукту
price = 100.0

# Різні типи знижок
no_discount = NoDiscount()
percentage_discount = PercentageDiscount(20)  # 20% знижки
fixed_discount = FixedAmountDiscount(15)      # Фіксована знижка 15

# Результати
print("Original price:", price)
print("No discount:", apply_discount(price, no_discount))
print("Percentage discount (20%):", apply_discount(price, percentage_discount))
print("Fixed discount ($15):", apply_discount(price, fixed_discount))

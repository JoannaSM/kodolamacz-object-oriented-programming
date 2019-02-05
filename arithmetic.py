from abc import ABC, abstractmethod
import math

class Node(ABC):

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Wykonuję {self.name}.", end=' ')

    @abstractmethod
    def value(self):
        pass


class Number(Node):
    def __init__(self, number):
        self.number = number
        super().__init__("liczba")

    def show(self):
        print(f"Jestem liczbą {self.number}")

    def value(self):
        return self.number


class Sum(Node):
    def __init__(self, component1, component2):
        self.component1 = component1
        self.component2 = component2
        super().__init__("dodawanie")

    def show(self):
        self.component1.show()
        self.component2.show()
        super().show()
        print(f"{self.component1.value()} + {self.component2.value()} = {self.value()}")

    def value(self):
        return self.component1.value() + self.component2.value()


class Diff(Node):

    def __init__(self, minuend, subtrahend):
        self.minuend = minuend
        self.subtrahend = subtrahend
        super().__init__("odejmowanie")

    def show(self):
        super().show()
        print(f"{self.minuend.value()} - {self.subtrahend.value()} = {self.value()}")

    def value(self):
        return self.minuend.value() - self.subtrahend.value()


class Multiplication(Node):

    def __init__(self, factor1, factor2):
        self.factor1 = factor1
        self.factor2 = factor2
        super().__init__("mnożenie")

    def show(self):
        super().show()
        print(f"{self.factor1.value()} * {self.factor2.value()} = {self.value()}")

    def value(self):
        return self.factor1.value() * self.factor2.value()


class Division(Node):

    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider
        super().__init__("dzielenie")

    def show(self):
        super().show()
        print(f"{self.dividend.value()} / {self.divider.value()} = {self.value()}")

    def value(self):
        return self.dividend.value() / self.divider.value()


class Factorial(Node):

    def __init__(self, number):
        self.number = number
        super().__init__("silnia")

    def show(self):
        super().show()
        print(f"{self.number.value()}! = {self.value()}")

    def value(self):
        return math.factorial(self.number.value())


def main():
    print("Wyrażenia arytmetyczne!!!")
    cztery = Number(4)
    piec = Number(5)
    szesc = Number(6)
    dwanascie = Number(12)

    suma = Sum(piec, cztery)
    suma.show()

    roznica = Diff(dwanascie, piec)
    roznica.show()

    mnozenie = Multiplication(cztery, szesc)
    mnozenie.show()

    dzielenie = Division(dwanascie, cztery)
    dzielenie.show()

    roznica = Diff(suma, mnozenie)
    roznica.show()

    silnia = Factorial(cztery)
    silnia.show()


if __name__ == "__main__":
    main()
from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def circumference(self):
        pass

    @abstractmethod
    def present(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Figure):

    def __init__(self, r):
        self.__r = r

    def circumference(self):
        return round(2 * math.pi * self.__r, 2)

    def present(self):
        print(f"Jestem kołem o promieniu {self.__r}")

    def area(self):
        return round(math.pi * self.__r**2, 2)


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.__edges = [a, b, c]
        self.__edges.sort()

        if sum(self.__edges[0:-1]) > self.__edges[2]:
            self.__correct = True
        else:
            self.__correct = False


    def circumference(self):
        if self.__correct:
            return sum(self.__edges)
        else:
            return None

    def present(self):
        if self.__correct:
            print(f"Jestem trójkątem o bokach: {self.__edges}")
        else:
            print(f"Z odcinków {self.__edges} nie da się zbudować trójkąta")

    def area(self):
        if self.__correct:
            p = 0.5 * sum(self.__edges)
            P = p * (p - self.__edges[0]) * (p - self.__edges[1]) * (p - self.__edges[2])
            P = math.sqrt(P)
            return round(P, 2)
        else:
            return None


class Rectangle(Figure):

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def circumference(self):
        return 2*(self._a+self._b)

    def present(self):
        print(f"Jestem prostokątem o wymiarach {self._a} x {self._b}")

    def area(self):
        return self._a * self._b


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)

    def present(self):
        print(f"Jestem kwadratem o boku {self._a}, czyli takim specjalnym prostokątem")


def main():
    figure_0 = Triangle(3, 3, 5)
    figure_0.present()
    print(f"Pole: {figure_0.area()}")
    print(f"Obwód: {figure_0.circumference()}\n")

    figure_1 = Triangle(3, 4, 10)
    figure_1.present()
    print(f"Pole: {figure_1.area()}")
    print(f"Obwód: {figure_1.circumference()}\n")

    figure_2 = Rectangle(2, 5)
    figure_2.present()
    print(f"Pole: {figure_2.area()}")
    print(f"Obwód: {figure_2.circumference()}\n")

    figure_3 = Square(6)
    figure_3.present()
    print(f"Pole: {figure_3.area()}")
    print(f"Obwód: {figure_3.circumference()}\n")

    figure_4 = Circle(3)
    figure_4.present()
    print(f"Pole: {figure_4.area()}")
    print(f"Obwód: {figure_4.circumference()}\n")


if __name__ == "__main__":
    main()
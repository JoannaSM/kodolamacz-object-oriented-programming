import math

class QuadraticFunction:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def solve(self):
        if self.__a == 0:
            if self.__b == 0:
                if self.__c == 0:
                    return 'Nieskończenie wiele rozwiązań'
                else:
                    return 'Brak rozwiązań'
            else:
                return round(-1*self.__c/self.__b,2)
        else:
            delta = self.__delta()
            if delta < 0:
                return 'Brak rozwiązań'
            else:
                x1 = round(-0.5*(self.__b - delta)/self.__a,2)
                x2 = round(-0.5*(self.__b + delta)/self.__a,2)
                if x1 != x2:
                    return [x1, x2]
                else:
                    return x1

    def show(self):
        print(f"równanie {self.__a}*x^2 {self.__b:+}*x {self.__c:+} = 0")

    def __delta(self):
        delta = self.__b**2 - 4*self.__a*self.__c
        if delta >= 0:
            return math.sqrt(delta)
        else:
            return -1


def main():
    case = QuadraticFunction(-2, -2, 1)
    case.show()
    print(case.solve())


if __name__ == "__main__":
    main()
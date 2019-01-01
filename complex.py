import math

class Complex:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return f"{self.re} {self.im:+}i"

    def module(self):
        return round(math.sqrt(self.re**2+self.im**2),2)

    @staticmethod
    def sum(nmb1, nmb2):
        re = round(nmb1.re+nmb2.re, 2)
        im = round(nmb1.im+nmb2.im, 2)

        return Complex(re, im)

    @staticmethod
    def quotient(nmb1, nmb2):
        re = round(nmb1.re*nmb2.re - nmb1.im*nmb2.im, 2)
        im = round(nmb1.re*nmb2.im + nmb1.im*nmb2.re, 2)
        return Complex(re,im)

def main():
    number1 = Complex(3.333, -5)
    number2 = Complex(-1, 12.777)

    module = number1.module()
    print(f"moduł: |{number1}| = {module}")
    module = number2.module()
    print(f"moduł: |{number2}| = {module}")

    sum = Complex.sum(number1, number2)
    print(f"suma: ({number1}) + ({number2}) = {sum}")

    quotient = Complex.quotient(number1,number2)
    print(f"iloczyn: ({number1}) * ({number2}) = {quotient}")


if __name__ == "__main__":
    main()
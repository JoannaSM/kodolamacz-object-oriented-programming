import math

class Fraction:

    def __init__(self, nom, denom):
        self.nom = nom
        self.denom = denom

    def __str__(self):
        return f"{self.nom}/{self.denom}"

    def simplify(self):
        found = False
        nom = math.fabs( self.nom )
        denom = math.fabs( self.denom )
        while not found:
            if nom == denom:
                found = True
            else:
                if nom > denom:
                    nom = nom - denom
                else:
                    denom = denom - nom
        else:
            self.nom = int(self.nom/nom)
            self.denom = int(self.denom/nom)

    @staticmethod
    def sum(numb1, numb2):
        denom = numb1.denom*numb2.denom
        nom = numb1.nom*numb2.denom + numb2.nom*numb1.denom
        return Fraction(nom, denom)

    @staticmethod
    def difference(numb1, numb2):
        denom = numb1.denom * numb2.denom
        nom = numb1.nom * numb2.denom - numb2.nom * numb1.denom
        return Fraction(nom, denom)

    @staticmethod
    def multiplication(numb1, numb2):
        nom = numb1.nom*numb2.nom
        denom = numb1.denom*numb2.denom
        return Fraction(nom, denom)

    @staticmethod
    def division(numb1, numb2):
        nom = numb1.nom*numb2.denom
        denom = numb1.denom*numb2.nom
        return Fraction(nom, denom)


def main():
    fract1 = Fraction(7, 21)
    print(f"ułamek: {fract1}")

    fract2 = Fraction(28, 70)
    print(f"ułamek: {fract2}")

    print("----\ndziałania:")
    sum = Fraction.sum(fract1, fract2)
    sum.simplify()
    print(f"{fract1} + {fract2} = {sum}")

    diff = Fraction.difference(fract1, fract2)
    diff.simplify()
    print(f"{fract1} - {fract2} = {diff}")

    multiplication = Fraction.multiplication(fract1, fract2)
    multiplication.simplify()
    print(f"{fract1} * {fract2} = {multiplication}")

    division = Fraction.division(fract1, fract2)
    division.simplify()
    print(f"{fract1} : {fract2} = {division}")

    print('----')
    print(f"skracanie {fract1}")
    fract1.simplify()
    print(fract1)
    print(f"skracanie {fract2}")
    fract2.simplify()
    print(fract2)


if __name__ == "__main__":
    main()
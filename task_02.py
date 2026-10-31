# Lekcja 09 — Zadanie 2: Kalkulator
class Kalkulator:
    def dodaj(self, a, b): return a + b
    def odejmij(self, a, b): return a - b
    def pomnoz(self, a, b): return a * b
    def podziel(self, a, b):
        if b == 0: raise ZeroDivisionError("Nie dziel przez zero")
        return a / b

k = Kalkulator()
for metoda in (k.dodaj, k.odejmij, k.pomnoz, k.podziel):
    print(metoda.__name__, metoda(12, 3))

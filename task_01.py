# Lekcja 09 — Zadanie 1: Produkt
class Produkt:
    def __init__(self, nazwa, cena, ilosc_w_magazynie):
        self.nazwa, self.cena, self.ilosc_w_magazynie = nazwa, cena, ilosc_w_magazynie

    def pokaz_info(self):
        print(f"{self.nazwa}: {self.cena:.2f} zł, stan: {self.ilosc_w_magazynie}")

    def sprzedaj(self, ilosc):
        if ilosc <= 0 or ilosc > self.ilosc_w_magazynie:
            raise ValueError("Nieprawidłowa ilość lub brak towaru")
        self.ilosc_w_magazynie -= ilosc

    def dostawa(self, ilosc):
        if ilosc <= 0:
            raise ValueError("Ilość musi być dodatnia")
        self.ilosc_w_magazynie += ilosc

produkty = [Produkt("Laptop", 3000, 4), Produkt("Mysz", 80, 12), Produkt("Monitor", 900, 6)]
for p in produkty:
    p.dostawa(2)
    p.sprzedaj(1)
    p.pokaz_info()

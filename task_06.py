# Lekcja 09 — Zadanie 6: Pojazd i Samochod
class Pojazd:
    def __init__(self, marka, model, rok):
        self.marka, self.model, self.rok = marka, model, rok

    def pokaz_info(self): print(f"{self.marka} {self.model}, rok {self.rok}")

class Samochod(Pojazd):
    def __init__(self, marka, model, rok, liczba_drzwi):
        super().__init__(marka, model, rok)
        self.liczba_drzwi = liczba_drzwi

    def pokaz_info(self):
        super().pokaz_info()
        print(f"Liczba drzwi: {self.liczba_drzwi}")

Samochod("Toyota", "Corolla", 2022, 5).pokaz_info()

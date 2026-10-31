# Lekcja 09 — Zadanie 16: Dziedziczenie wielopoziomowe
class Zwierze:
    def __init__(self, nazwa, wiek): self.nazwa, self.wiek = nazwa, wiek
    def pokaz_info(self): print(f"Nazwa: {self.nazwa}, wiek: {self.wiek}")

class Ssak(Zwierze):
    def __init__(self, nazwa, wiek, typ_futra):
        super().__init__(nazwa, wiek)
        self.typ_futra = typ_futra
    def pokaz_info(self):
        super().pokaz_info()
        print(f"Typ futra: {self.typ_futra}")

class Pies(Ssak):
    def __init__(self, nazwa, wiek, typ_futra, rasa):
        super().__init__(nazwa, wiek, typ_futra)
        self.rasa = rasa
    def pokaz_info(self):
        super().pokaz_info()
        print(f"Rasa: {self.rasa}")

Pies("Reks", 4, "krótkie", "beagle").pokaz_info()

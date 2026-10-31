# Lekcja 09 — Zadanie 17: Rezerwacje hotelowe
from datetime import date

class Pokoj:
    def __init__(self, numer, typ, cena_za_noc, zajety=False):
        self.numer, self.typ, self.cena_za_noc, self.zajety = numer, typ, cena_za_noc, zajety

class Rezerwacja:
    def __init__(self, pokoj, data_od, data_do, gosc):
        self.pokoj, self.data_od, self.data_do, self.gosc = pokoj, data_od, data_do, gosc
    def koszt(self): return (self.data_do-self.data_od).days * self.pokoj.cena_za_noc

class Hotel:
    def __init__(self, pokoje=None, rezerwacje=None):
        self.pokoje = list(pokoje) if pokoje is not None else []
        self.rezerwacje = list(rezerwacje) if rezerwacje is not None else []
    def dodaj_pokoj(self, pokoj):
        if any(p.numer == pokoj.numer for p in self.pokoje): raise ValueError("Numer pokoju zajęty")
        self.pokoje.append(pokoj)
    def rezerwuj(self, numer_pokoju, gosc, data_od, data_do):
        pokoj = next((p for p in self.pokoje if p.numer == numer_pokoju), None)
        if pokoj is None or data_od >= data_do: raise ValueError("Nieprawidłowy pokój lub daty")
        if pokoj.zajety or any(r.pokoj is pokoj and data_od < r.data_do and data_do > r.data_od for r in self.rezerwacje):
            raise ValueError("Pokój niedostępny w podanym terminie")
        rezerwacja = Rezerwacja(pokoj, data_od, data_do, gosc)
        self.rezerwacje.append(rezerwacja)
        pokoj.zajety = True  # uproszczenie: zajęty = ma rezerwację
        return rezerwacja
    def wolne_pokoje(self): return [p for p in self.pokoje if not p.zajety]
    def przychod(self): return sum(r.koszt() for r in self.rezerwacje)

hotel = Hotel()
for i in range(1, 11): hotel.dodaj_pokoj(Pokoj(i, "standard" if i <= 7 else "premium", 200 if i <= 7 else 350))
for i in range(1, 6): hotel.rezerwuj(i, f"Gość {i}", date(2026, 11, i), date(2026, 11, i+2))
print("Wolne pokoje:", [p.numer for p in hotel.wolne_pokoje()])
print(f"Przychód: {hotel.przychod():.2f} zł")

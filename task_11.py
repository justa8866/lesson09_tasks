# Lekcja 09 — Zadanie 11: System ocen uczniow
class Uczen:
    def __init__(self, imie, oceny=None):
        self.imie = imie
        self.oceny = list(oceny) if oceny is not None else []
    def srednia(self): return sum(self.oceny)/len(self.oceny) if self.oceny else 0

class Klasa:
    def __init__(self, nazwa, uczniowie=None):
        self.nazwa = nazwa
        self.uczniowie = list(uczniowie) if uczniowie is not None else []
    def dodaj_ucznia(self, uczen): self.uczniowie.append(uczen)
    def srednia_klasy(self):
        oceny = [o for u in self.uczniowie for o in u.oceny]
        return sum(oceny)/len(oceny) if oceny else 0
    def najlepszy_uczen(self):
        kandydaci = [u for u in self.uczniowie if u.oceny]
        return max(kandydaci, key=lambda u: u.srednia()) if kandydaci else None

klasa = Klasa("3A")
for imie, oceny in [("Anna", [5, 5]), ("Jan", [3, 4]), ("Ola", [4, 5]), ("Piotr", [3, 3]), ("Ewa", [5, 4])]:
    klasa.dodaj_ucznia(Uczen(imie, oceny))
print(f"Średnia klasy: {klasa.srednia_klasy():.2f}")
print("Najlepszy uczeń:", klasa.najlepszy_uczen().imie)

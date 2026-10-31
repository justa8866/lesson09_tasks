# Lekcja 09 — Zadanie 19: Gra RPG
class Postac:
    def __init__(self, imie, hp, atak, obrona):
        self.imie, self.hp, self.atak, self.obrona = imie, hp, atak, obrona
        self.max_hp = hp
    def atakuj(self, cel):
        if self.hp <= 0: return
        obrazenia = max(1, self.atak-cel.obrona)
        cel.hp = max(0, cel.hp-obrazenia)
        print(f"{self.imie} atakuje {cel.imie}: -{obrazenia} HP (pozostało {cel.hp})")
    def leczenie(self, punkty):
        if punkty < 0: raise ValueError("Punkty muszą być nieujemne")
        self.hp = min(self.max_hp, self.hp+punkty)

class Wojownik(Postac):
    def __init__(self, imie): super().__init__(imie, 120, 25, 12)

class Mag(Postac):
    def __init__(self, imie): super().__init__(imie, 80, 12, 5)
    def rzuc_czar(self, cel):
        if self.hp <= 0: return
        obrazenia = max(1, 35-cel.obrona//2)
        cel.hp = max(0, cel.hp-obrazenia)
        print(f"{self.imie} rzuca czar na {cel.imie}: -{obrazenia} HP")

class Lucznik(Postac):
    def __init__(self, imie):
        super().__init__(imie, 90, 18, 7)
        self.szybkosc = 2
    def szybki_atak(self, cel):
        for _ in range(self.szybkosc):
            if cel.hp > 0: self.atakuj(cel)

wojownik, mag, lucznik = Wojownik("Thor"), Mag("Merlin"), Lucznik("Robin")
wojownik.atakuj(mag)
mag.rzuc_czar(wojownik)
lucznik.szybki_atak(wojownik)
mag.leczenie(15)
wojownik.atakuj(lucznik)
for p in (wojownik, mag, lucznik): print(f"{p.imie}: {p.hp}/{p.max_hp} HP")

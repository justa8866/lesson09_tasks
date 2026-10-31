# Lekcja 09 — Zadanie 4: Ksiazka
class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania, liczba_stron):
        self.tytul, self.autor, self.rok_wydania, self.liczba_stron = tytul, autor, rok_wydania, liczba_stron

    def __str__(self):
        return f"{self.tytul} — {self.autor} ({self.rok_wydania}), {self.liczba_stron} stron"

ksiazki = [Ksiazka("Lalka", "B. Prus", 1890, 680), Ksiazka("Dziady", "A. Mickiewicz", 1832, 300), Ksiazka("Solaris", "S. Lem", 1961, 240), Ksiazka("Quo vadis", "H. Sienkiewicz", 1896, 500), Ksiazka("Ferdydurke", "W. Gombrowicz", 1937, 280)]
for ksiazka in ksiazki: print(ksiazka)

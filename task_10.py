# Lekcja 09 — Zadanie 10: Zamowienie z kompozycja
class Produkt:
    def __init__(self, nazwa, cena): self.nazwa, self.cena = nazwa, cena

class Zamowienie:
    def __init__(self): self.produkty = []
    def dodaj_produkt(self, produkt, ilosc):
        if ilosc <= 0: raise ValueError("Ilość musi być dodatnia")
        self.produkty.append((produkt, ilosc))
    def laczna_wartosc(self): return sum(p.cena * n for p, n in self.produkty)
    def pokaz_zamowienie(self):
        for p, n in self.produkty: print(f"{p.nazwa}: {n} × {p.cena:.2f} = {n*p.cena:.2f} zł")
        print(f"Razem: {self.laczna_wartosc():.2f} zł")

z = Zamowienie()
for nazwa, cena, ilosc in [("Chleb", 6, 2), ("Mleko", 4, 3), ("Ser", 12, 1), ("Jabłka", 5, 2), ("Kawa", 30, 1)]:
    z.dodaj_produkt(Produkt(nazwa, cena), ilosc)
z.pokaz_zamowienie()

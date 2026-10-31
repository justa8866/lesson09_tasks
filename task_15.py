# Lekcja 09 — Zadanie 15: Portfel inwestycyjny
class Akcja:
    def __init__(self, nazwa, cena_kupna, cena_aktualna):
        self.nazwa, self.cena_kupna, self.cena_aktualna = nazwa, cena_kupna, cena_aktualna

class Portfel:
    def __init__(self, kapital_poczatkowy, akcje=None):
        self.kapital_poczatkowy = kapital_poczatkowy
        self.gotowka = kapital_poczatkowy
        self.akcje = dict(akcje) if akcje is not None else {}
    def kup_akcje(self, akcja, ilosc):
        koszt = akcja.cena_aktualna * ilosc
        if ilosc <= 0 or koszt > self.gotowka: raise ValueError("Brak środków lub niepoprawna ilość")
        self.gotowka -= koszt
        self.akcje[akcja] = self.akcje.get(akcja, 0) + ilosc
    def sprzedaj_akcje(self, akcja, ilosc):
        if ilosc <= 0 or ilosc > self.akcje.get(akcja, 0): raise ValueError("Brak akcji")
        self.gotowka += ilosc * akcja.cena_aktualna
        self.akcje[akcja] -= ilosc
        if self.akcje[akcja] == 0: del self.akcje[akcja]
    def aktualizuj_ceny(self, slownik_cen):
        for akcja in self.akcje:
            if akcja.nazwa in slownik_cen: akcja.cena_aktualna = slownik_cen[akcja.nazwa]
    def wartosc_portfela(self): return self.gotowka + sum(a.cena_aktualna*n for a, n in self.akcje.items())
    def zysk_strata(self): return self.wartosc_portfela() - self.kapital_poczatkowy

p = Portfel(10000)
akcje = [Akcja(n, c, c) for n, c in [("AAA", 100), ("BBB", 200), ("CCC", 50), ("DDD", 80), ("EEE", 120)]]
for a in akcje: p.kup_akcje(a, 5)
p.aktualizuj_ceny({"AAA": 110, "BBB": 180, "CCC": 65, "DDD": 75, "EEE": 140})
p.sprzedaj_akcje(akcje[0], 2)
p.sprzedaj_akcje(akcje[2], 1)
print(f"Wartość portfela (wraz z gotówką): {p.wartosc_portfela():.2f} zł")
print(f"Zysk/strata: {p.zysk_strata():+.2f} zł")

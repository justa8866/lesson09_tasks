# Lekcja 09 — Zadanie 9: Pipeline z wieloma krokami
class FiltrowanieDodatnich:
    def wykonaj(self, dane): return [x for x in dane if x >= 0]

class Zaokraglanie:
    def wykonaj(self, dane): return [round(x) for x in dane]

class Skalowanie:
    def __init__(self, wspolczynnik): self.wspolczynnik = wspolczynnik
    def wykonaj(self, dane): return [x * self.wspolczynnik for x in dane]

class Sumowanie:
    def wykonaj(self, dane): return sum(dane)

class Pipeline:
    def __init__(self, kroki): self.kroki = kroki
    def uruchom(self, dane):
        for krok in self.kroki: dane = krok.wykonaj(dane)
        return dane

pipeline = Pipeline([FiltrowanieDodatnich(), Zaokraglanie(), Skalowanie(2), Sumowanie()])
print("Wynik:", pipeline.uruchom([1.7, -3.2, 5.8, -1.1, 8.3, 2.4]))

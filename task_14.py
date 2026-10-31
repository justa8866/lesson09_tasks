# Lekcja 09 — Zadanie 14: Pipeline ML
import math

class LogTransformer:
    def transform(self, dane):
        if any(x <= -1 for x in dane): raise ValueError("log(x+1) wymaga x > -1")
        return [math.log1p(x) for x in dane]

class OutlierRemover:
    def transform(self, dane):
        if not dane: return []
        srednia = sum(dane)/len(dane)
        std = (sum((x-srednia)**2 for x in dane)/len(dane))**0.5
        return [x for x in dane if abs(x-srednia) <= 3*std]

class BinningTransformer:
    def __init__(self, granice): self.granice = sorted(granice)
    def transform(self, dane): return [sum(x >= granica for granica in self.granice) for x in dane]

class Pipeline:
    def __init__(self, kroki): self.kroki = kroki
    def transform(self, dane):
        for krok in self.kroki: dane = krok.transform(dane)
        return dane

dane = [1, 5, 10, 100, 2, 3, 8, 200, 4, 6]
pipeline = Pipeline([OutlierRemover(), LogTransformer(), BinningTransformer([1, 2, 3, 4])])
print("Wejście:", dane)
print("Wynik (numery przedziałów):", pipeline.transform(dane))

# Lekcja 09 — Zadanie 18: Walidacja danych
import math

class ValidatorZakresu:
    def __init__(self, min, max): self.min, self.max = min, max
    def sprawdz(self, dane):
        ok = all(isinstance(x, (int, float)) and not isinstance(x, bool) and self.min <= x <= self.max for x in dane)
        return ok, "Wszystkie wartości w zakresie" if ok else "Wartość poza zakresem lub nie jest liczbą"

class ValidatorTypu:
    def __init__(self, typ): self.typ = typ
    def sprawdz(self, dane):
        ok = all(isinstance(x, self.typ) for x in dane)
        return ok, "Typy poprawne" if ok else "Nieprawidłowy typ"

class ValidatorBrakow:
    def sprawdz(self, dane):
        ok = all(x is not None and not (isinstance(x, float) and math.isnan(x)) for x in dane)
        return ok, "Brak braków" if ok else "Wykryto None/NaN"

class Pipeline:
    def __init__(self, walidatory): self.walidatory = walidatory
    def sprawdz(self, dane):
        wyniki = [w.sprawdz(dane) for w in self.walidatory]
        return all(ok for ok, _ in wyniki), wyniki

p = Pipeline([ValidatorBrakow(), ValidatorTypu((int, float)), ValidatorZakresu(0, 100)])
for dane in ([10, 20, 30], [10, None, float("nan"), 200]):
    print("Dane:", dane, "Wynik:", p.sprawdz(dane))

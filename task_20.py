# Lekcja 09 — Zadanie 20: Ekosystem transformerow
class BaseTransformer:
    def transform(self, dane): raise NotImplementedError

class DropNullTransformer(BaseTransformer):
    def transform(self, dane): return [x for x in dane if x is not None]

class ClipTransformer(BaseTransformer):
    def __init__(self, min, max):
        if min > max: raise ValueError("min > max")
        self.min, self.max = min, max
    def transform(self, dane): return [max(self.min, min(self.max, x)) for x in dane]

class SquareTransformer(BaseTransformer):
    def transform(self, dane): return [x*x for x in dane]

class InverseTransformer(BaseTransformer):
    def transform(self, dane):
        if 0 in dane: raise ZeroDivisionError("Nie można odwrócić zera")
        return [1/x for x in dane]

class Pipeline:
    def __init__(self, transformery): self.transformery = transformery
    def fit_transform(self, dane):
        for transformer in self.transformery: dane = transformer.transform(dane)
        return dane

dane = [None, -3, 0, 2, 5, 12]
pipeline = Pipeline([DropNullTransformer(), ClipTransformer(1, 10), SquareTransformer(), InverseTransformer()])
print("Wejście:", dane)
print("Wynik:", pipeline.fit_transform(dane))

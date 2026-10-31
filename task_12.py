# Lekcja 09 — Zadanie 12: FiguraGeometryczna
from math import pi

class Figura:
    def pole(self): raise NotImplementedError

class Prostokat(Figura):
    def __init__(self, szerokosc, wysokosc): self.szerokosc, self.wysokosc = szerokosc, wysokosc
    def pole(self): return self.szerokosc * self.wysokosc

class Kolo(Figura):
    def __init__(self, promien): self.promien = promien
    def pole(self): return pi * self.promien**2

figury = [Prostokat(3, 4), Kolo(2), Prostokat(5, 6), Kolo(1)]
for figura in figury: print(type(figura).__name__, f"pole = {figura.pole():.2f}")
print(f"Łączne pole: {sum(f.pole() for f in figury):.2f}")

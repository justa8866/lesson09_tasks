# Lekcja 09 — Zadanie 7: Pracownik
class Pracownik:
    def __init__(self, imie, stanowisko, pensja):
        self.imie, self.stanowisko, self.pensja = imie, stanowisko, pensja

    def podwyzka(self, procent):
        if procent < 0: raise ValueError("Procent nie może być ujemny")
        self.pensja *= 1 + procent / 100

    def __str__(self): return f"{self.imie}, {self.stanowisko}: {self.pensja:.2f} zł"

pracownicy = [Pracownik("Anna", "Analityk", 6000), Pracownik("Jan", "Programista", 8000), Pracownik("Ola", "Tester", 5500)]
for p, procent in zip(pracownicy, (10, 5, 8)):
    p.podwyzka(procent)
    print(p)

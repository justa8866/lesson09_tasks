# Lekcja 09 — Zadanie 8: Lista TODO
class Zadanie:
    def __init__(self, opis, status="do zrobienia"):
        self.opis, self.status = opis, status

    def oznacz_jako_zrobione(self): self.status = "zrobione"
    def __str__(self): return f"[{self.status}] {self.opis}"

zadania = [Zadanie(opis) for opis in ("Nauka", "Zakupy", "Spacer", "Projekt", "Powtórka")]
for i in (0, 2, 4): zadania[i].oznacz_jako_zrobione()
for zadanie in zadania: print(zadanie)

# Lekcja 09 — Zadanie 5: Student
class Student:
    def __init__(self, imie, numer_indeksu, oceny=None):
        self.imie, self.numer_indeksu = imie, numer_indeksu
        self.oceny = list(oceny) if oceny is not None else []

    def dodaj_ocene(self, ocena):
        if not 2 <= ocena <= 5: raise ValueError("Ocena poza zakresem 2–5")
        self.oceny.append(ocena)

    def srednia(self): return sum(self.oceny) / len(self.oceny) if self.oceny else 0
    def __str__(self): return f"{self.imie} ({self.numer_indeksu}), średnia: {self.srednia():.2f}"

studenci = [Student("Anna", 101), Student("Jan", 102), Student("Ola", 103)]
for student, oceny in zip(studenci, ([4, 5, 4], [3, 4, 3], [5, 5, 4])):
    for ocena in oceny: student.dodaj_ocene(ocena)
    print(student)

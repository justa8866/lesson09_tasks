# Lekcja 09 — Zadanie 13: System biblioteki
class Ksiazka:
    def __init__(self, tytul, autor, dostepna=True):
        self.tytul, self.autor, self.dostepna = tytul, autor, dostepna

class Uzytkownik:
    def __init__(self, imie, wypozyczone_ksiazki=None):
        self.imie = imie
        self.wypozyczone_ksiazki = list(wypozyczone_ksiazki) if wypozyczone_ksiazki is not None else []

class Biblioteka:
    def __init__(self, ksiazki=None, uzytkownicy=None):
        self.ksiazki = list(ksiazki) if ksiazki is not None else []
        self.uzytkownicy = list(uzytkownicy) if uzytkownicy is not None else []
    def dodaj_ksiazke(self, ksiazka): self.ksiazki.append(ksiazka)
    def zarejestruj_uzytkownika(self, uzytkownik): self.uzytkownicy.append(uzytkownik)
    def wypozycz(self, uzytkownik, ksiazka):
        if uzytkownik not in self.uzytkownicy or ksiazka not in self.ksiazki or not ksiazka.dostepna:
            raise ValueError("Nie można wypożyczyć książki")
        ksiazka.dostepna = False
        uzytkownik.wypozyczone_ksiazki.append(ksiazka)
    def zwroc(self, uzytkownik, ksiazka):
        if ksiazka not in uzytkownik.wypozyczone_ksiazki: raise ValueError("Użytkownik nie ma tej książki")
        uzytkownik.wypozyczone_ksiazki.remove(ksiazka)
        ksiazka.dostepna = True
    def raport(self):
        print(f"Książek: {len(self.ksiazki)}, dostępnych: {sum(k.dostepna for k in self.ksiazki)}, użytkowników: {len(self.uzytkownicy)}")
        for u in self.uzytkownicy: print(u.imie, [k.tytul for k in u.wypozyczone_ksiazki])

b = Biblioteka()
for i in range(10): b.dodaj_ksiazke(Ksiazka(f"Książka {i+1}", f"Autor {i+1}"))
for imie in ("Anna", "Jan", "Ola"): b.zarejestruj_uzytkownika(Uzytkownik(imie))
for i in range(6): b.wypozycz(b.uzytkownicy[i % 3], b.ksiazki[i])
b.zwroc(b.uzytkownicy[0], b.ksiazki[0])
b.raport()

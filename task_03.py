# Lekcja 09 — Zadanie 3: BankAccount
class BankAccount:
    def __init__(self, wlasciciel, saldo=0):
        if saldo < 0: raise ValueError("Saldo początkowe nie może być ujemne")
        self.wlasciciel, self.saldo = wlasciciel, saldo

    def wplac(self, kwota):
        if kwota <= 0: raise ValueError("Kwota musi być dodatnia")
        self.saldo += kwota

    def wyplac(self, kwota):
        if kwota <= 0 or kwota > self.saldo: raise ValueError("Nieprawidłowa kwota lub brak środków")
        self.saldo -= kwota

    def pokaz_saldo(self): print(f"{self.wlasciciel}: {self.saldo:.2f} zł")

konta = [BankAccount("Anna", 500), BankAccount("Jan", 1000), BankAccount("Ola", 200)]
for konto in konta:
    konto.wplac(100)
    konto.wyplac(50)
    konto.pokaz_saldo()

# US-02-07 Lista uczestników

- **Epika:** [EPIC-02](README.md)
- **Aktor:** Trener, Admin
- **Priorytet:** Could

## Historyjka
Jako trener chcę zobaczyć listę uczestników moich zajęć, aby wiedzieć, kto przyjdzie.

## Co widać
- imię i nazwisko każdej osoby z rezerwacją **Aktywna**
- liczba zapisanych, np. „Zapisanych: 8 z 12”

## Kryteria akceptacji
| # | Sytuacja | Wynik |
|---|---|---|
| 1 | Trener otwiera swoje zajęcia | lista osób z aktywną rezerwacją |
| 2 | Ktoś anulował rezerwację | ta osoba znika z listy |
| 3 | Nikt się nie zapisał | komunikat „Brak zapisanych osób” |
| 4 | Trener otwiera cudze zajęcia | odmowa (brak uprawnień) |
| 5 | Admin otwiera dowolne zajęcia | widzi listę |
| 6 | Klient próbuje otworzyć listę | odmowa (brak uprawnień) |

## Powiązane
Z7, [US-02-02](US-02-02-zapis-na-zajecia.md), [US-02-03](US-02-03-anulowanie-rezerwacji.md)

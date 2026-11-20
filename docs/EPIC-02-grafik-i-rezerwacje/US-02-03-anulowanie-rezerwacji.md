# US-02-03 Anulowanie rezerwacji

- **Epika:** [EPIC-02](README.md)
- **Aktor:** Klient, Admin
- **Priorytet:** Must

## Historyjka
Jako klient chcę anulować swoją rezerwację, aby zwolnić miejsce i odzyskać wejście, gdy nie mogę przyjść.

Jako admin chcę anulować rezerwację za klienta, np. gdy klient zadzwoni na recepcję.

## Kryteria akceptacji
| # | Sytuacja | Wynik |
|---|---|---|
| 1 | Aktywna, co najmniej 12 h przed zajęciami, karnet ilościowy | **Anulowana**, miejsce wraca, wejście wraca |
| 2 | Aktywna, co najmniej 12 h przed zajęciami, karnet czasowy | **Anulowana**, miejsce wraca |
| 3 | Aktywna, mniej niż 12 h przed zajęciami | odmowa: „Za późno na anulowanie” |
| 4 | Zajęcia już się zaczęły lub odbyły (dotyczy też admina) | odmowa |
| 5 | Rezerwacja już anulowana lub odwołana | brak przycisku, a próba przez API kończy się odmową |
| 6 | Klient próbuje anulować cudzą rezerwację | odmowa (brak uprawnień) |
| 7 | Admin anuluje za klienta przed rozpoczęciem zajęć, także mniej niż 12 h przed nimi | **Anulowana**, miejsce i wejście wracają |
| 8 | Po anulowaniu | klient może zapisać się ponownie (patrz US-02-02, scenariusz 9) |

## Powiązane
BR-07, Z5, [US-02-02](US-02-02-zapis-na-zajecia.md)

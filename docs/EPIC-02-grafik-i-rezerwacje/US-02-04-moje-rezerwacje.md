# US-02-04 Moje rezerwacje

- **Epika:** [EPIC-02](README.md)
- **Aktor:** Klient
- **Priorytet:** Should

## Historyjka
Jako klient chcę widzieć listę swoich rezerwacji, aby wiedzieć, na jakie zajęcia mam miejsce.

## Kryteria akceptacji
| # | Sytuacja | Co widać |
|---|---|---|
| 1 | Nadchodzące rezerwacje | lista od najbliższej: zajęcia, data, godzina, trener |
| 2 | Aktywna rezerwacja, do zajęć zostało co najmniej 12 h | przycisk „Anuluj” |
| 3 | Aktywna rezerwacja, do zajęć zostało mniej niż 12 h | brak przycisku, informacja „Nie można już anulować” |
| 4 | Studio odwołało zajęcia, które miały się dopiero odbyć | rezerwacja zostaje w nadchodzących z etykietą „Odwołane”, bez przycisku „Anuluj” |
| 5 | Historia | rezerwacje Anulowane i Odbyte oraz Odwołane z minionych dat, każda ze statusem |
| 6 | Brak jakichkolwiek rezerwacji | komunikat i link do grafiku |
| 7 | Klient widzi tylko swoje rezerwacje | rezerwacje innych osób są niedostępne |

Scenariusz 4 jest ważny, bo w v1 nie ma powiadomień mailowych. Klient dowie się o odwołaniu tylko z tej listy albo z grafiku.

## Powiązane
BR-07, [US-02-03](US-02-03-anulowanie-rezerwacji.md), [US-02-06](US-02-06-odwolanie-zajec.md)

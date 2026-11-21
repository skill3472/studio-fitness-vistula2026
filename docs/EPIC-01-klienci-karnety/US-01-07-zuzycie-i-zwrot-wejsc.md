# US-01-07 Zużycie i zwrot wejść

- **Epika:** [EPIC-01](README.md)
- **Aktor:** System EPIC-02
- **Priorytet:** Must

## Historyjka

Jako system chcę odejmować wejście po zapisie i oddawać je po dozwolonym anulowaniu, aby stan karnetu był poprawny.

## Kryteria akceptacji

| # | Sytuacja | Wynik |
| --- | --- | --- |
| 1 | Udany zapis klienta z karnetem ilościowym (5 wejść) | rezerwacja aktywna, zostają 4 wejścia |
| 2 | Udany zapis klienta z karnetem czasowym | rezerwacja aktywna, brak odejmowania wejść |
| 3 | Zapis się nie udał, np. brak miejsca | liczba wejść się nie zmienia |
| 4 | Klient anuluje rezerwację co najmniej 12 h przed zajęciami | rezerwacja anulowana, zużyte wejście wraca |
| 5 | Admin anuluje rezerwację przed zajęciami | zużyte wejście wraca także poniżej 12 h |
| 6 | Admin odwołuje całe zajęcia przed rozpoczęciem | wejścia wracają wszystkim z aktywnymi rezerwacjami ilościowymi |
| 7 | Ta sama rezerwacja została już rozliczona | ponowne żądanie nie odejmuje ani nie zwraca wejścia drugi raz |

## Powiązane

BR-01-06, BR-01-07, EPIC-02 / US-02-02, US-02-03, US-02-06.


# US-01-04 Przypisywanie karnetu

- **Epika:** [EPIC-01](README.md)
- **Aktor:** Admin
- **Priorytet:** Must

## Historyjka

Jako admin chcę przypisać klientowi karnet, aby mógł zapisywać się na zajęcia.

## Dane przypisania

- klient
- rodzaj karnetu
- data początku i końca ważności

## Kryteria akceptacji

| # | Sytuacja | Wynik |
| --- | --- | --- |
| 1 | Admin przypisuje poprawny karnet ilościowy | karnet pojawia się u klienta z pełną liczbą wejść |
| 2 | Admin przypisuje karnet czasowy | karnet pojawia się u klienta z datami ważności |
| 3 | Klient ma już aktywny karnet | odmowa: „Klient ma już aktywny karnet” |
| 4 | Data końca jest wcześniejsza niż data początku | odmowa: „Niepoprawny okres ważności” |
| 5 | Osoba bez roli admina próbuje przypisać karnet | odmowa (brak uprawnień) |
| 6 | Wskazany klient nie istnieje | odmowa: „Nie znaleziono klienta” |

## Powiązane

Z2, Z3, BR-01-02, BR-01-03, [US-01-05](US-01-05-moj-karnet.md).


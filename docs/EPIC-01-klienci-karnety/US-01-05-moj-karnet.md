# US-01-05 Mój karnet

- **Epika:** [EPIC-01](README.md)
- **Aktor:** Klient
- **Priorytet:** Must

## Historyjka

Jako klient chcę sprawdzić swój karnet, aby wiedzieć, czy mogę zapisać się na zajęcia.

## Co widać

- nazwa i rodzaj karnetu
- daty ważności
- dla ilościowego: liczba pozostałych wejść

## Kryteria akceptacji

| # | Sytuacja | Co widać |
| --- | --- | --- |
| 1 | Klient ma ważny karnet ilościowy | nazwa, daty i liczba pozostałych wejść, np. „5 z 8” |
| 2 | Klient ma ważny karnet czasowy | nazwa, daty i informacja „Bez limitu wejść” |
| 3 | Klient nie ma karnetu | „Nie masz aktywnego karnetu” |
| 4 | Karnet stracił ważność | oznaczenie „Wygasły” |
| 5 | Klient próbuje podejrzeć cudzy karnet | odmowa (brak uprawnień) |

## Powiązane

Z1, Z4, [US-01-06](US-01-06-sprawdzanie-karnetu.md).

# US-01-06 Sprawdzanie karnetu przy zapisie

- **Epika:** [EPIC-01](README.md)
- **Aktor:** System EPIC-02
- **Priorytet:** Must

## Historyjka

Jako system rezerwacji chcę sprawdzić karnet klienta przed zapisem, aby nie dopuścić do rezerwacji bez ważnego karnetu.

## Kryteria akceptacji

| # | Sytuacja | Wynik |
| --- | --- | --- |
| 1 | Karnet ilościowy jest ważny w dniu zajęć i ma wolne wejście | zapis może być kontynuowany |
| 2 | Karnet czasowy jest ważny w dniu zajęć | zapis może być kontynuowany |
| 3 | Klient nie ma aktywnego karnetu | odmowa: „Nie masz aktywnego karnetu” |
| 4 | Karnet nie obejmuje daty zajęć | odmowa: „Karnet nie obejmuje tej daty” |
| 5 | Karnet ilościowy ma 0 wejść | odmowa: „Brak wolnych wejść na karnecie” |

## Powiązane

BR-01-04, BR-01-05, EPIC-02 / US-02-02.

**Uwaga:** EPIC-02 sprawdza termin, kolizje i wolne miejsca; EPIC-01 sprawdza tylko karnet. Ostateczne sprawdzenie wejścia odbywa się też w chwili jego zużycia.

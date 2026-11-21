# US-01-01 Rejestracja klienta

- **Epika:** [EPIC-01](README.md)
- **Aktor:** Gość
- **Priorytet:** Must

## Historyjka

Jako gość chcę utworzyć konto w studiu fitness, aby móc otrzymać karnet i zapisywać się na zajęcia.

## Kryteria akceptacji

| # | Sytuacja | Wynik |
| --- | --- | --- |
| 1 | Gość podaje imię, nazwisko, poprawny e-mail i hasło | konto klienta zostaje utworzone |
| 2 | Brakuje wymaganego pola | odmowa i informacja o brakującym polu |
| 3 | E-mail jest już zajęty | odmowa: „Konto z tym e-mailem już istnieje” |
| 4 | Niepoprawny format e-maila | odmowa: „Niepoprawny e-mail” |
| 5 | Nowy klient nie ma jeszcze karnetu | konto działa, ale zapis na zajęcia nie jest możliwy bez karnetu |

## Powiązane

BR-01-01, [US-01-04](US-01-04-przypisywanie-karnetu.md), EPIC-02 / US-02-02.

# US-02-05 Zarządzanie grafikiem

- **Epika:** [EPIC-02](README.md)
- **Aktor:** Admin
- **Priorytet:** Must

## Historyjka
Jako admin chcę dodawać, edytować i usuwać terminy zajęć, aby grafik był aktualny.

## Dane terminu
| Pole | Wymagane | Uwagi |
|---|---|---|
| Rodzaj zajęć | tak | z listy rodzajów, np. Joga |
| Data | tak | nie w przeszłości |
| Godzina od / do | tak | „do” później niż „od” |
| Trener | tak | z listy kont trenerów |
| Sala | tak | z listy sal |
| Limit miejsc | tak | co najmniej 1 |

## Kryteria akceptacji
| # | Sytuacja | Wynik |
|---|---|---|
| 1 | Poprawny nowy termin | pojawia się w grafiku |
| 2 | Brak wymaganego pola | odmowa ze wskazaniem, którego pola brakuje |
| 3 | Termin w przeszłości | odmowa |
| 4 | Limit mniejszy niż 1 | odmowa |
| 5 | Koniec zajęć przed ich początkiem | odmowa |
| 6 | Trener prowadzi w tym czasie inne zajęcia (Should) | odmowa: „Trener jest zajęty w tym czasie” |
| 7 | W tej sali są w tym czasie inne zajęcia (Should) | odmowa: „Sala jest zajęta w tym czasie” |
| 8 | Zwiększenie limitu | więcej wolnych miejsc w grafiku |
| 9 | Zmniejszenie limitu, ale nie poniżej liczby zapisanych | dozwolone |
| 10 | Zmniejszenie limitu poniżej liczby zapisanych | odmowa |
| 11 | Zmiana daty lub godziny, gdy nikt nie jest zapisany | dozwolona |
| 12 | Zmiana daty lub godziny, gdy są zapisani | odmowa: „Odwołaj zajęcia i dodaj nowy termin” |
| 13 | Zmiana trenera lub sali, gdy są zapisani | dozwolona, rezerwacje zostają |
| 14 | Usunięcie terminu bez żadnych rezerwacji | termin znika z grafiku |
| 15 | Usunięcie terminu z rezerwacjami (także anulowanymi) | odmowa: „Odwołaj zajęcia zamiast usuwać” |
| 16 | Klient lub trener próbuje edytować grafik | odmowa (brak uprawnień) |

## Powiązane
BR-08, BR-09, BR-10, Z7, [US-02-06](US-02-06-odwolanie-zajec.md)

# US-02-02 Zapis na zajęcia

- **Epika:** [EPIC-02](README.md)
- **Aktor:** Klient
- **Priorytet:** Must

## Historyjka
Jako klient chcę zapisać się na wybrane zajęcia, aby mieć zagwarantowane miejsce.

## Kryteria akceptacji
| # | Sytuacja | Wynik |
|---|---|---|
| 1 | Wszystko w porządku, karnet ilościowy | rezerwacja **Aktywna**, wolnych miejsc o 1 mniej, zużyte 1 wejście |
| 2 | Wszystko w porządku, karnet czasowy | rezerwacja **Aktywna**, wolnych miejsc o 1 mniej, wejścia się nie liczą |
| 3 | Niezalogowany | przekierowanie do logowania |
| 4 | Brak karnetu albo karnet nieaktywny | odmowa: „Nie masz aktywnego karnetu” |
| 5 | Karnet wygasa przed dniem zajęć | odmowa: „Karnet nie obejmuje tej daty” |
| 6 | Karnet ilościowy z 0 wejść | odmowa: „Brak wolnych wejść na karnecie” |
| 7 | Brak wolnych miejsc | odmowa: „Brak wolnych miejsc” |
| 8 | Klient ma już rezerwację na ten termin | odmowa: „Masz już rezerwację na te zajęcia” |
| 9 | Klient wcześniej anulował ten termin | zapis dozwolony, jeśli są miejsca |
| 10 | Zajęcia już się zaczęły lub minęły | odmowa: „Zapisy na te zajęcia są zamknięte” |
| 11 | Zajęcia odwołane | odmowa: „Zajęcia zostały odwołane” |
| 12 | Klient ma inne zajęcia w tym samym czasie (Should) | odmowa: „Masz w tym czasie inne zajęcia” |
| 13 | Zapis mniej niż 12 h przed zajęciami | zapis dozwolony, z ostrzeżeniem, że tej rezerwacji nie da się już anulować |
| 14 | Dwie osoby w tej samej chwili biorą ostatnie miejsce | jedna dostaje rezerwację, druga widzi „Brak wolnych miejsc” |

## Kolejność sprawdzania
Gdy kilka warunków jest niespełnionych naraz, system pokazuje komunikat pierwszego z nich:
1. Czy użytkownik jest zalogowany
2. Czy termin istnieje, nie jest odwołany i jeszcze się nie zaczął
3. Czy klient nie ma już rezerwacji na ten termin
4. Czy klient nie ma w tym czasie innych zajęć
5. Czy karnet jest ważny w dniu zajęć i ma wolne wejście
6. Czy są wolne miejsca

## Uwaga dla backendu
Sprawdzenie wolnych miejsc, utworzenie rezerwacji i zużycie wejścia z karnetu muszą być jedną operacją (transakcją). Inaczej scenariusz 14 przepuści dwie osoby na jedno miejsce, a dwa jednoczesne zapisy na różne zajęcia zużyją to samo ostatnie wejście.

## Powiązane
BR-01 do BR-07, Z1, Z2, Z4, Z6, EPIC-01 (dane karnetu)

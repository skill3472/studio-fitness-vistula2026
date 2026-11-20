# US-02-01 Przeglądanie grafiku

- **Epika:** [EPIC-02](README.md)
- **Aktor:** Gość, Klient
- **Priorytet:** Must

## Historyjka
Jako gość lub klient chcę przeglądać grafik zajęć na najbliższe dni, aby wybrać zajęcia i sprawdzić, czy są wolne miejsca.

## Co widać przy każdym terminie
- rodzaj zajęć
- data oraz godzina rozpoczęcia i zakończenia
- trener
- liczba wolnych miejsc, np. „Wolne: 5 z 12”
- przycisk „Zapisz” albo informacja o stanie (patrz tabela)

## Kryteria akceptacji
| # | Sytuacja | Co widać |
|---|---|---|
| 1 | Otwarcie grafiku | terminy od dziś na 14 dni, posortowane według daty i godziny |
| 2 | Zwykły termin z wolnymi miejscami | wszystkie dane terminu i przycisk „Zapisz” |
| 3 | Brak wolnych miejsc | „Brak miejsc”, przycisk zapisu nieaktywny |
| 4 | Zajęcia odwołane | oznaczenie „Odwołane”, brak przycisku |
| 5 | Zajęcia, które już się zaczęły | nie są pokazywane |
| 6 | Zalogowany klient ma rezerwację na ten termin | „Zapisano” zamiast „Zapisz” |
| 7 | Osoba niezalogowana | widzi grafik, „Zapisz” prowadzi do logowania |
| 8 | Dzień bez zajęć | komunikat „Brak zajęć tego dnia” |
| 9 | Filtr po rodzaju zajęć lub trenerze (Should) | tylko pasujące terminy |
| 10 | Filtr, do którego nic nie pasuje | komunikat „Brak zajęć dla wybranych filtrów” |

## Powiązane
Z3, Z4, BR-05, [US-02-02](US-02-02-zapis-na-zajecia.md)

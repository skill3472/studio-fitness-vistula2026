# EPIC-02 Grafik i rezerwacje

**Cel:** klient widzi ofertę zajęć i liczbę wolnych miejsc, może się zapisać i anulować rezerwację, a system pilnuje limitu uczestników.

## Aktorzy
- **Gość (niezalogowany)**: tylko przegląda grafik.
- **Klient**: przegląda grafik, zapisuje się, anuluje swoje rezerwacje.
- **Admin (recepcja)**: układa grafik, odwołuje zajęcia, może anulować rezerwację za klienta.
- **Trener**: widzi listę uczestników swoich zajęć.

## Pojęcia
| Pojęcie | Znaczenie | Przykład |
|---|---|---|
| Rodzaj zajęć | co to za zajęcia | Joga, Crossfit |
| Termin zajęć | konkretne zajęcia w grafiku: data, godzina, trener, sala, limit miejsc | Joga, wt. 18:00, limit 12 |
| Rezerwacja | zapis klienta na konkretny termin | Jan zapisany na Jogę we wt. 18:00 |

Trening personalny to po prostu termin z limitem 1 miejsca, więc nie potrzebuje osobnego modułu.

## Założenia (do potwierdzenia z Product Ownerem)
| Nr | Założenie |
|---|---|
| Z1 | Karnet jest ilościowy (np. 8 wejść) albo czasowy (np. miesiąc bez limitu). Szczegóły należą do EPIC-01. |
| Z2 | Zapis od razu zużywa 1 wejście z karnetu ilościowego. |
| Z3 | Grafik pokazuje 14 dni do przodu, licząc od dziś. |
| Z4 | Grafik widzi każdy. Zapis wymaga zalogowania. |
| Z5 | Admin może anulować rezerwację w każdej chwili przed rozpoczęciem zajęć. Wejście zawsze wraca. |
| Z6 | Klient ma najwyżej jeden aktywny karnet naraz. Przy zapisie system sprawdza właśnie ten karnet. |
| Z7 | Rodzaje zajęć, sale i konta trenerów są wprowadzone do systemu na starcie. Trener musi mieć konto, żeby widzieć swoje zajęcia (US-02-07). |

## Reguły biznesowe
| Nr | Reguła |
|---|---|
| BR-01 | Liczba aktywnych rezerwacji na termin nie może przekroczyć limitu miejsc. |
| BR-02 | Klient ma najwyżej 1 aktywną rezerwację na dany termin. |
| BR-03 | Do zapisu potrzebny jest karnet ważny **w dniu zajęć**, nie tylko dzisiaj. |
| BR-04 | Karnet ilościowy musi mieć co najmniej 1 wolne wejście. |
| BR-05 | Nie można zapisać się na zajęcia, które już się zaczęły albo zostały odwołane. |
| BR-06 | Klient nie może mieć dwóch rezerwacji na zajęcia, które nakładają się w czasie (Should). |
| BR-07 | Klient może anulować rezerwację najpóźniej 12 h przed zajęciami. Wtedy wejście wraca. |
| BR-08 | Termin, na który jest jakakolwiek rezerwacja (także anulowana), można tylko odwołać, nie usunąć. |
| BR-09 | Limitu miejsc nie można zmniejszyć poniżej liczby zapisanych osób. |
| BR-10 | Terminowi, na który ktoś jest zapisany, nie można zmienić daty ani godziny. Trzeba go odwołać i dodać nowy. |

## Statusy rezerwacji
| Status | Kiedy | Czy wejście wraca |
|---|---|---|
| Aktywna | po udanym zapisie | nie dotyczy |
| Anulowana | klient anulował co najmniej 12 h przed zajęciami albo anulował admin przed ich rozpoczęciem | tak |
| Odwołana | admin odwołał zajęcia | tak |
| Odbyta | zajęcia minęły | nie |

Rezerwacja Aktywna może przejść w każdy z pozostałych statusów. Innych przejść nie ma.

Statusu „Odbyta” nie zapisujemy w bazie, tylko go wyliczamy: rezerwacja jest Aktywna, a zajęcia już minęły.

## Historyjki
| Nr | Historyjka | Aktor | Priorytet |
|---|---|---|---|
| [US-02-01](US-02-01-przegladanie-grafiku.md) | Przeglądanie grafiku | Gość, Klient | Must |
| [US-02-02](US-02-02-zapis-na-zajecia.md) | Zapis na zajęcia | Klient | Must |
| [US-02-03](US-02-03-anulowanie-rezerwacji.md) | Anulowanie rezerwacji | Klient, Admin | Must |
| [US-02-04](US-02-04-moje-rezerwacje.md) | Moje rezerwacje | Klient | Should |
| [US-02-05](US-02-05-zarzadzanie-grafikiem.md) | Zarządzanie grafikiem | Admin | Must |
| [US-02-06](US-02-06-odwolanie-zajec.md) | Odwołanie zajęć | Admin | Should |
| [US-02-07](US-02-07-lista-uczestnikow.md) | Lista uczestników | Trener, Admin | Could |

## Zależności
- **EPIC-01 (klienci i karnety):** ważność karnetu i liczba wejść. Potrzebne w US-02-02, US-02-03 i US-02-06.
- **Logowanie i role:** odróżnienie gościa, klienta, admina i trenera.

## Poza zakresem v1
Lista rezerwowa, zajęcia cykliczne (np. „co wtorek”), powiadomienia mailowe, oznaczanie nieobecności, płatności online, zarządzanie salami, rodzajami zajęć i trenerami.

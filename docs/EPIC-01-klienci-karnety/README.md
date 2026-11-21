# EPIC-01 Klienci i karnety

**Cel:** Klient może utworzyć konto, sprawdzić swój karnet oraz liczbę pozostałych wejść. Admin (recepcja) zarządza klientami, rodzajami karnetów i przypisaniem karnetów. System pilnuje ważności karnetu i prawidłowo rozlicza wejścia podczas rezerwacji zajęć z EPIC-02.

## Aktorzy

- **Gość (niezalogowany):** może się zarejestrować i zalogować; nie widzi danych klientów ani ich karnetów.
- **Klient:** widzi swój profil, rodzaje karnetów, własny karnet i dostępne wejścia. Zapisuje się na zajęcia w EPIC-02.
- **Admin (recepcja):** przegląda konta klientów, definiuje rodzaje karnetów i przypisuje karnety klientom.
- **System rezerwacji (EPIC-02):** sprawdza karnet przy zapisie oraz zleca zużycie lub zwrot wejścia.

## Pojęcia

| Pojęcie | Znaczenie | Przykład |
| --- | --- | --- |
| Klient | osoba z kontem w studiu | Jan Kowalski |
| Karnet ilościowy | karnet z ustaloną liczbą wejść | 8 wejść |
| Karnet czasowy | karnet bez limitu wejść w okresie ważności | 30 dni |
| Karnet klienta | rodzaj karnetu przypisany konkretnej osobie | karnet Jana, ważny do 30.11 |

## Założenia

| Nr | Założenie |
| --- | --- |
| Z1 | Są dwa rodzaje karnetów: **ilościowy** (np. 8 wejść) i **czasowy** (np. miesiąc bez limitu). Jak w Z1 EPIC-02. |
| Z2 | Karnety przypisuje klientom **admin**. Nie robimy zakupów ani płatności online. (do potwierdzenia) |
| Z3 | Klient może mieć najwyżej **jeden aktywny karnet naraz**. Jak w Z6 EPIC-02. |
| Z4 | Karnet ma datę początku i końca ważności. Musi obejmować **dzień wybranych zajęć**. |
| Z5 | Udany zapis **od razu zużywa 1 wejście** z karnetu ilościowego; czasowy nie ma licznika. Jak w Z2 EPIC-02. |
| Z6 | Dozwolone anulowanie rezerwacji lub odwołanie zajęć zwraca zużyte wejście zgodnie z EPIC-02. |
| Z7 | Logowanie i role są wspólne dla całego systemu; rodzaje karnetów są wprowadzone na starcie (bez panelu do edycji oferty). |

## Reguły biznesowe

| Nr | Reguła |
| --- | --- |
| BR-01-01 | Jeden adres e-mail może mieć tylko jedno konto klienta. |
| BR-01-02 | Tylko admin przypisuje karnet klientowi. |
| BR-01-03 | Klient ma najwyżej jeden aktywny karnet naraz. |
| BR-01-04 | Zapis wymaga karnetu ważnego w dniu zajęć. |
| BR-01-05 | Karnet ilościowy musi mieć co najmniej 1 wolne wejście. |
| BR-01-06 | Udana rezerwacja zużywa dokładnie 1 wejście ilościowe; dla karnetu czasowego niczego nie odejmuje. |
| BR-01-07 | Po dozwolonym anulowaniu lub odwołaniu zajęć wejście wraca **tylko raz**, jeśli wcześniej zostało zużyte. |

## Historyjki użytkownika

| ID | Historyjka | Aktor | Priorytet |
| --- | --- | --- | --- |
| [US-01-01](US-01-01-rejestracja-klienta.md) | Rejestracja klienta | Gość | Must |
| [US-01-02](US-01-02-moje-dane.md) | Moje dane | Klient | Should |
| [US-01-03](US-01-03-rodzaje-karnetow.md) | Rodzaje karnetów | Klient | Must |
| [US-01-04](US-01-04-przypisywanie-karnetu.md) | Przypisywanie karnetu | Admin | Must |
| [US-01-05](US-01-05-moj-karnet.md) | Mój karnet | Klient | Must |
| [US-01-06](US-01-06-sprawdzanie-karnetu.md) | Sprawdzanie karnetu przy zapisie | System EPIC-02 | Must |
| [US-01-07](US-01-07-zuzycie-i-zwrot-wejsc.md) | Zużycie i zwrot wejść | System EPIC-02 | Must |

## Powiązanie z EPIC-02

| Akcja w EPIC-02 | Co robi EPIC-01 |
| --- | --- |
| US-02-02 Zapis na zajęcia | Sprawdza karnet i zużywa wejście przy udanym zapisie. |
| US-02-03 Anulowanie rezerwacji | Zwraca zużyte wejście, jeśli anulowanie jest dozwolone: klient co najmniej 12 h przed zajęciami, admin przed ich rozpoczęciem. |
| US-02-06 Odwołanie zajęć | Zwraca wejścia wszystkim klientom z aktywnymi rezerwacjami na odwołane zajęcia. |

**Podział odpowiedzialności:** EPIC-02 obsługuje grafik, dostępne miejsca i rezerwacje. EPIC-01 obsługuje konta klientów, karnety i saldo wejść.

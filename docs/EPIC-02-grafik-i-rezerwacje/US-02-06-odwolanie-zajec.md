# US-02-06 Odwołanie zajęć

- **Epika:** [EPIC-02](README.md)
- **Aktor:** Admin
- **Priorytet:** Should

## Historyjka
Jako admin chcę odwołać zajęcia, aby zapisani klienci wiedzieli, że zajęcia się nie odbędą, i odzyskali wejścia.

## Kryteria akceptacji
| # | Sytuacja | Wynik |
|---|---|---|
| 1 | Odwołanie zajęć z zapisanymi | wszystkie Aktywne rezerwacje zmieniają status na **Odwołana**, wejścia wracają |
| 2 | Odwołanie zajęć bez zapisanych | termin oznaczony jako odwołany |
| 3 | Po odwołaniu | termin zostaje w grafiku z oznaczeniem „Odwołane”, zapis niemożliwy |
| 4 | Odwołanie zajęć, które już się zaczęły lub minęły | odmowa |
| 5 | Ponowne odwołanie już odwołanych zajęć | odmowa (nic się nie zmienia) |

## Powiązane
BR-05, BR-08, BR-10, [US-02-05](US-02-05-zarzadzanie-grafikiem.md), [US-02-04](US-02-04-moje-rezerwacje.md)

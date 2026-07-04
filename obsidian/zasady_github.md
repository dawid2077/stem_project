# Zasady pracy z Git i GitHub

## Główne zasady

### Nie pushujemy bezpośrednio do `main`

Wszystkie zmiany trafiają do projektu przez **Pull Request (PR)**.

Schemat pracy:

1. Pobierz najnowsze zmiany z `main`.
2. Utwórz lub przełącz się na swoją gałąź.
3. Wprowadź zmiany.
4. Wykonaj commit(y).
5. Wypchnij gałąź na GitHub.
6. Otwórz Pull Request.
7. Po akceptacji zmiany zostaną zmergowane do `main`.

> **Nigdy nie wykonujemy `git push` bezpośrednio do gałęzi `main`.**

---

## Commity

Starajcie się robić **małe i częste commity**.

Lepiej:
- ✅ 5 commitów po jednej konkretnej zmianie

niż:
- ❌ 1 ogromny commit zawierający wszystko.

Dzięki temu łatwiej:
- znaleźć błędy,
- przejrzeć zmiany,
- cofnąć pojedynczą funkcjonalność, jeśli zajdzie taka potrzeba.

---

## Pull Requesty

Każdy commit powinien finalnie trafić do projektu przez **Pull Request**.

Przy tworzeniu PR:
- dodaj krótki opis, **co zostało zmienione**,
- jeśli coś wymaga uwagi lub testów — napisz o tym,
- nie zostawiaj pustych opisów.

Nie musi to być długi tekst — kilka zdań w zupełności wystarczy.

---

## Aktualizowanie swojej gałęzi

Regularnie pobieraj najnowsze zmiany z `main`, aby uniknąć konfliktów.

Najprościej:

```bash
git pull origin main
```

Dobrą praktyką jest wykonanie tego przed rozpoczęciem pracy oraz przed otwarciem Pull Requesta.

---

## CodeRabbit

Do Pull Requestów jest automatycznie podłączony **CodeRabbit**.

Będzie komentował kod i sugerował możliwe poprawki.

Ja z niego korzystam na co dzień, ale decyzja, czy będziecie go używać również u siebie, należy do Was.
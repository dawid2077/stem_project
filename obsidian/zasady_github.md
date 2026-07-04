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

- ✅ 5 commitów po jednej konkretnej zmianie,

niż:

- ❌ 1 ogromny commit zawierający wiele różnych zmian.

Dzięki temu łatwiej:

- znaleźć błędy,
- przejrzeć zmiany,
- cofnąć pojedynczą funkcjonalność,
- zrozumieć historię projektu.

---

## Pull Requesty

Każda zmiana trafia do projektu przez **Pull Request**.

Przy tworzeniu PR:

- dodaj krótki opis, **co zostało zmienione**,
- jeśli coś wymaga uwagi lub testów — napisz o tym,
- nie zostawiaj pustych opisów.
- po skończeniu pull requesta usun gałąz którą używałeś

Nie musi to być długi tekst — kilka zdań w zupełności wystarczy.

### Merge

Do łączenia zmian z `main` używamy wyłącznie:

> **Squash and Merge**

Dzięki temu historia gałęzi `main` pozostaje czytelna i składa się z jednego commita na każdy zaakceptowany Pull Request.

---

## Labels

Korzystamy z **GitHub Labels** do oznaczania Pull Requestów oraz Issue.

Przykładowe zastosowania:

- `frontend`
- `backend`
- `bug`
- `enhancement`
- `documentation`
- `AI`
- `help wanted`

Jeżeli zauważycie, że przydałaby się nowa kategoria, śmiało twórzcie **własne (autorskie) labelki**. Mają one ułatwiać organizację projektu, więc nie bójcie się ich rozwijać.

---

## Aktualizowanie swojej gałęzi

Regularnie pobieraj najnowsze zmiany z `main`, aby uniknąć konfliktów.

Najprościej:

```bash
git pull origin main
```

Dobrą praktyką jest wykonanie tego:

- przed rozpoczęciem pracy,
- przed otwarciem Pull Requesta,
- po zmergowaniu większych zmian przez innych członków zespołu.

---

## CodeRabbit

Do Pull Requestów jest automatycznie podłączony **CodeRabbit**.

Będzie komentował kod i sugerował możliwe poprawki.

Ja korzystam z niego na co dzień, ale decyzja, czy będziecie używać go również u siebie, należy do Was.
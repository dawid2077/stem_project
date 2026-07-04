# 🎓 Nazwa Projektu

> *Do ustalenia*

Asystent AI odpowiadający na pytania dotyczące rekrutacji, zapisów oraz innych informacji związanych z uczelnią.

Projekt realizowany jest jako aplikacja we Flutterze z backendem w FastAPI. Model LLM działa po stronie backendu, a frontend komunikuje się z nim wyłącznie poprzez REST API.

---

# 🛠 Tech Stack

## Frontend

- Flutter (Web-first, z zachowaniem kompatybilności z Android/iOS)

## Backend

- Python
- FastAPI

## AI

- Model LLM jako część backendu

---

# 📌 Roadmap

## ✅ Faza 1 — MVP (Minimum Viable Product)

Minimalna wersja aplikacji powinna umożliwiać komunikację użytkownika z modelem AI.

### Frontend (Flutter)

- Strona główna.
- Sekcja **Chat**.
- Po wejściu do chatu przejście na:

```text
/chat
```

- Pole do wpisywania wiadomości.
- Po wysłaniu wiadomości wykonywany jest request:

```http
POST /chat/stream
```

zgodny ze schematem zdefiniowanym w modelach **Pydantic**.

- Odpowiedź z backendu jest odbierana jako **stream**.
- Wiadomość AI wyświetlana jest użytkownikowi na bieżąco — słowo po słowie lub kolejnymi chunkami.

### Backend

Backend powinien:

- udostępniać endpoint `POST /chat/stream`,
- obsługiwać komunikację z modelem LLM,
- zwracać odpowiedź w postaci streamu.

> Model LLM jest częścią backendu. Frontend komunikuje się wyłącznie z API.

### Wymagania dotyczące Fluttera

Aplikacja będzie rozwijana przede wszystkim pod **Flutter Web**, jednak kod powinien być pisany w sposób umożliwiający bezproblemowe uruchomienie również na urządzeniach mobilnych (Android/iOS), bez tworzenia osobnych wersji aplikacji.

---

## 🚧 Faza 2

Rozszerzenie funkcjonalności czatu.

- zapisywanie historii rozmowy,
- przesyłanie historii wiadomości do backendu,
- możliwość prowadzenia wieloetapowych konwersacji.

---

## 🚧 Faza 3

Rozszerzenie możliwości modelu AI.

### Opcjonalnie — RAG (Retrieval-Augmented Generation)

Model LLM będzie mógł korzystać z dodatkowego kontekstu w postaci:

- PDF-ów,
- regulaminów,
- informacji o rekrutacji,
- informacji o rejestracji,
- innych materiałów uczelni.

Dzięki temu odpowiedzi będą bardziej precyzyjne i oparte na rzeczywistych źródłach.

> Implementacja RAG jest opcjonalnym rozszerzeniem projektu i nie jest wymagana do ukończenia MVP.

---

## 🚧 Faza 4

Model AI generuje podsumowanie całej rozmowy.

Użytkownik może pobrać wygenerowane podsumowanie bezpośrednio z aplikacji Flutter.

---

# 📋 Aktualne zadania

## Frontend

- stworzenie aplikacji we Flutterze zgodnie z wymaganiami MVP,
- implementacja ekranu czatu,
- obsługa streamowania odpowiedzi z backendu,
- integracja z REST API.

## Backend

- rozwój REST API w FastAPI,
- integracja modelu LLM,
- obsługa streamowania odpowiedzi.

## Dane

Pozyskanie materiałów wykorzystywanych przez model AI:

- PDF-ów,
- informacji z uczelni,
- dokumentów dotyczących rekrutacji,
- dokumentów dotyczących rejestracji,
- innych przydatnych materiałów.

## Projekt

- wymyślenie nazwy projektu,
- przygotowanie logo.

## Architektura

Przygotowanie diagramu architektury projektu (np. w **draw.io**) przedstawiającego:

- frontend,
- backend,
- model LLM,
- opcjonalny moduł RAG,
- przepływ danych pomiędzy komponentami.

---

# 📌 Organizacja pracy

## GitHub Projects

Zakładka **Projects**  (a tam Tablica_Stem) służy do organizacji pracy zespołu.

Dodawajcie tam:

- zadania,
- pomysły,
- propozycje nowych funkcjonalności,
- bugi,
- rzeczy, nad którymi aktualnie pracujecie,
- kwestie wymagające omówienia.

Dzięki temu każdy będzie wiedział, nad czym pracuje reszta zespołu i co jest aktualnie do zrobienia.

---

## Git i GitHub

Zasady pracy z repozytorium znajdują się w pliku:

```text
obsidian/zasady_github.md
```

Obowiązują wszystkich członków zespołu.

---

# 👥 Podział ról

| Osoba | Odpowiedzialność |
|--------|------------------|
| Grzesiu | Flutter (Frontend) |
| Kamil | Flutter (Frontend) |
| Dawid | FastAPI, Backend, GitHub, zarządzanie projektem |
| Patryk | Do ustalenia (prawdopodobnie Frontend) |

---

# 💡 Filozofia projektu

To nie jest lista sztywnych zasad — jeśli macie dobre pomysły, dopisujcie je.

## Roadmap 
Załozenia projektu i roadmap są elastyczne zmieniajmy je jak uważamy 

## Frontend

napiszcie jaki zamierzacie frontend zrobic mi sie wydaje ze frontend bedzie najwazniejszy i jego wyglad i efekt wow musimy nam to wygrac

## Dzielmy się wiedzą

Poza kodem warto dzielić się również:

- dokumentacją,
- własnymi notatkami,
- ciekawymi narzędziami,
- bibliotekami,
- artykułami,
- poradnikami,
- dobrymi praktykami.

Im więcej wiedzy zostanie w projekcie, tym łatwiej będzie go rozwijać i utrzymywać.

## Git i GitHub

Jeżeli ktoś dopiero zaczyna pracę z Gitem lub GitHubem, warto poświęcić trochę czasu na poznanie podstaw.

Znajomość branchy, commitów i Pull Requestów znacznie ułatwi współpracę całemu zespołowi.

---

# 📄 Licencja

Projekt jest udostępniany na licencji **GNU Affero General Public License v3.0 (AGPL-3.0)**.

Szczegóły znajdują się w pliku `LICENSE`.

Copyright © 2026 dawid2077
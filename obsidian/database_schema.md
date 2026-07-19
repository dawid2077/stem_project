
BAZA DANYCH SQLITE KONCEPT

unikalne id uczelni od 0 do 999
/data

    - 001 uniwersytet_warszawski_dynamic.md ( wtym regulamin info o rekrutacji itp na samej gorze krotka notka tego typu ID_UCZELNI: 001 NAZWA MIASTO: TYP: LINK_REKRUTACJA: )
    - 001 uniwersytet_warszawski_static.md (podzial na dane zmieniajaace sie i stale)
    - 002 uniwersytet_jagielonski_dynamic.md
    - 002 uniwersytet_jagielonski_static.md



format bedzie .md


uzywajac md

(llm mi to wygenerowal)
to:

co w tym:
Sekcja 1: Ogólne informacje i lokalizacja

    Dokładny adres (przydatne, jeśli ktoś pyta: „która uczelnia jest najbliżej dworca?”).

    Opis kampusu (czy akademiki są blisko wydziałów, czy rozsiane po całym mieście).

    Krótki opis klimatu uczelni (np. nowoczesna, sportowa, historyczna).

Sekcja 2: Kierunki studiów (Kluczowe!)

    Lista wydziałów i kierunków.

    Progi punktowe z zeszłego roku (ludzie potwornie często o to pytają: „gdzie się dostanę z matmą na 60%?”).

    Opłaty za czesne (jeśli studia są płatne/niestacjonarne).

Sekcja 3: Finanse i wsparcie

    Stypendia (socjalne, naukowe, rektora – kwoty i progi dochodowe).

    Ceny i dostępność akademików.

Sekcja 4: Życie studenckie i opinie

    Koła naukowe, sekcje sportowe.

    Wymiany międzynarodowe (Erasmus – z jakimi krajami mają umowy).

    Skrócone opinie studentów (można zrobić mały zbiór z forum/Reddita typu: „plusy: super atmosfera, minusy: dziekanat to koszmar”).


albo to (albo oba):
# SEKCJA 1: INFORMACJE OGÓLNE I DANE KONTAKTOWE
(Adresy, dziekanaty, godziny otwarcia, ogólny opis uczelni)

# SEKCJA 2: REKRUTACJA I PROGI PUNKTOWE
(Wymagania, przedmioty maturalne, limity miejsc, progi z zeszłych lat)

# SEKCJA 3: KIERUNKI STUDIÓW I OPŁATY
(Lista kierunków, podział na wydziały, cennik czesnego za studia zaoczne)

# SEKCJA 4: STYPENDIA I POMOC FINANSOWA
(Stypendia socjalne, naukowe, zapomogi, progi dochodowe)

# SEKCJA 5: AKADEMIKI I ZAKWATEROWANIE
(Domy studenckie, ceny za pokój, kryteria przyznawania miejsc)

# SEKCJA 6: REGULAMIN STUDIÓW (PRAWA I OBOWIĄZKI)
(Zaliczenia, sesja, warunki, rezygnacje, skreślenia z listy studentów)

# SEKCJA 7: ŻYCIE STUDENCKIE I ERASMUS
(Koła naukowe, sport, wymiany zagraniczne, opinie studentów)





sqlite schema

users – podstawowe informacje o użytkowniku tabela


CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    google_id TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    display_name TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME DEFAULT CURRENT_TIMESTAMP
);

(zrezygnowalem z home city id narazie, dla mvp uzywam tylko google sign in )




(NAJWAZNIEJSZA !!) Tabela universities (Uczelnie) (NAJWAZNIEJSZA !!)

CREATE TABLE universities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    aliases TEXT,
    province TEXT,
    type TEXT,
    main_website TEXT,
    original_urls TEXT,             -- Linki do PDF-ów rozdzielone przecinkami
    md_path_dynamic TEXT NOT NULL, -- Ścieżka do pliku _dynamic.md
    md_path_static TEXT NOT NULL,  -- Ścieżka do pliku _static.md
    last_updated TEXT               -- Format YYYY-MM-DD
);


---
to moze w przyszlosci bo nie chce komplikowac:

miasta:
id INTEGER PRIMARY KEY AUTOINCREMENT, -- SQLite radzi sobie idealnie z prostym ID liczbowym
  name TEXT NOT NULL UNIQUE,            -- Zapewnia, że nie dodasz dwa razy tego samego miasta
  latitude REAL NOT NULL,               -- REAL to odpowiednik double/float w SQLite
  longitude REAL NOT NULL,


Zamiast promienia użytkownik wskazuje konkretne miasta, do których jest gotów dojechać.

```sql
create table user_preferred_cities (
  user_id uuid references users(id) on delete cascade,
  city_id uuid references cities(id) on delete cascade,
  primary key (user_id, city_id)
);




a to pomine bo ripgrep wystarczy poza tym ai ma spory kontekst window



Przechowuje poziom, tryb, kierunki, ale też luźne zainteresowania i przedmioty szkolne wskazane przez ucznia (nie muszą być od razu wiązane z konkretnymi kierunkami).
```sql
create table user_university_preferences (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id) on delete cascade unique, -- jeden zestaw na użytkownika
  degree_levels text[],        -- np. {'licencjat', 'inżynier'}
  study_modes text[],          -- np. {'stacjonarne'}
  liked_school_subjects text[], -- np. {'matematyka', 'informatyka'}
  general_interests text[],     -- np. {'sztuczna inteligencja', 'psychologia'}
  additional_criteria jsonb,   -- np. {'max_tuition': 5000, 'tags': ['internat']}
  updated_at timestamptz default now()
);
```

#### `user_memories` – pamięć długoterminowa dla LLM
Tutaj model zapisuje istotne fakty o użytkowniku, które nie pasują do innych tabel.
```sql
create table user_memories (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id) on delete cascade,
  key text,                     -- np. 'preferencje_transportowe', 'sytuacja_rodzinna'
  value text,                   -- treść pamięci
  importance smallint default 1,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);
```


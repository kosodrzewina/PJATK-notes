# WSI

## 003 koncepcja modelu relacyjnego bazy danych

**Edgar Frank "Ted" Codd** - brytyjski informatyk znany przede wszystkim ze swojego wkładu do rozwoju teorii relacyjnych baz danych.

### Najważniejsze założenia modelu relacyjnego

- Wszystkie dane zapisywane są w postaci tabel
- W tabeli znajdują się kolumny zawierające dane określonego typu
- W komórce tabeli (na przecięciu wierszy) znajduje się pojedyncza wartość, atomowa, niepodzielna

**Klucz główny** - jeden lub więcej kolumn, w których wartości jednoznacznie identyfikują cały wiersz (rekord). Wartość klucza głównego zawsze musi być określona i (z definicji) nie może się powtarzać - musi być unikalny.

**Klucz obcy** - jedna lub więcej kolumn, których wartości występują jako wartości ustalonego klucza głównego lub jednoznacznego w jednej tabeli i są interpretowane jako wskaźniki do wierszy w drugiej tabeli.

Dodaje się tabelę łączącą (asocjacyjną), kiedy relacje występują jako (wiele do wiele/niejednoznaczne).

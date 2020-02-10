# projektowanie baz danych

## Etapy projektowania bazy danych

- Etap projektu koncepcyjnego - określanie zapotrzebowanie biznesowe na projekt. Jest to etap rozeznania marketingowego, mającego dać odpowiedź na pytanie jakich funkcji produktu oczekuje klient, jakie funkcje są mu niezbędne do prowadzenia działań.
- Etap projektowania logicznego - etap, w którym planuje się ogólną strukturę.
- Etap projektowania fizycznego - model koncepcyjny przekłada się na model techniczny.

## Analiza przed przystąpieniem do projektowania bazy danych

- Co jest przedmiotem projektu
- Jaki jest cel projektu, jakie problemy projekt ma rozwiązać lub usprawnić działanie rozwiązań dotychczasowych
- Jakie funkcje będę realizowane w ramach projektu
- Kto te funkcje będzie wykorzystywał
- Jakie informacje (pod postacią danych) muszą być przechowywane w bazie danych aby powyższe założenia mogły zostać zrealizowane
- Jaki jest przewidywany aspekt ekonomiczny całego przedsięwzięcia

**Diagram przypadków użycia** (use case)

**Diagram związków encji** (entity relationship diagram) - model, który leży w obszarze zainteresowań systemu, jak też struktury bazy danych. Określa jednoznacznie potrzeby użytkownika. Umożliwia sprawdzenie czy analityk systemu dobrze zrozumiał intencję użytkownika. Jest znacznie prostszy niż sama baza danych.

**Narzędzie CASE** (Computer Aided Software Engineering) - graficzne narzędzia do projektowania baz danych.

**Encja** - byt, coś co istnieje, jest odróżnialne od innych bytów, co da się opisać, o czym informację można poznać i przechować. Rozróżniamy ją jako typ (klasę) obiektów oraz instancję encji, jako pojedyncze wystąpienie obiektu (pojedynczy egzemplarz) danego typu.

**Atrybuty encji** - abstrakcyjne cechy, a nie konkretne wartości.

## Encja jest w postaci normalnej, jeśli:
- Opisuje jeden typ obiektów
- Wartości atrybutów są elementarne (atomowe, niepodzielne)
- Nie zawiera kolekcji (powtarzających się grup informacji
- Posiada klucz
- Kolejność atrybutów może być dowolna, ich kolejność nie może kodować żadnych informacji

**Związek** - uporządkowana lista encji. Poszczególne encje mogą występować w niej wielokrotnie. Każdy związek określa pewną zależność między zbiorami egzemplarzy. 

**Związek binarny** - związek, który tworzą dwie encje, Jest ona reprezentowana graficznie jako linia łącząca dwie ramki (encje).

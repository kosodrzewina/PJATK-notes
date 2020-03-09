# RBD

## 002 relacyjny model danych

W matematyce **relację** definiuje się jako podzbiór **iloczynu kartezjańskiego**. Tabela jest logiczną reprezentacją relacji.

Iloczyn kartezjański nie jest przemienny: $A \times B \neq B \times A$

### Poziomy abstrakcji bazy danych

- **poziom użytkowy** - perspektywa użytkownika, sposób w jaki użytkownik postrzega dane.
- **poziom logiczny** (koncepcyjny) - zbiór tabel, powiązanych związkami, oraz innych obiektów, gwarantujących spójność logiczną oraz powiązanie ich wartości z miejscem zapisu na dusku (dyskach).
- **poziom fizyczny** - zbiór plików w systemie plików, w których dane przechowywane są fizycznie.

**Więzy spójności** (constraints) - zbiór reguł, których zadaniem jest zagwarantowanie logicznej poprawności danych przechowywanych w bazie. Szczególną cechą więzów spójności jest to, że są definiowane na etapie projektowania bazy danych, a za ich realizację (przestrzeganie reguł) odpowiada SZBD.

### Postulaty Codda

#### 0

System zarządzania bazą danych można uznać za system relacyjny (RBDBMS) wówczas, gdy w celu zarządzania bazą danych wykorzystuje wyłącznie rozwiązania zgodne z modelem relacyjnym.

#### 1 - postulat informacyjny

Na poziomie logicznym wszystkie dane (łącznie z nazwami tabel i kolumn), reprezentowane są wyłącznie za pomocą wartości w tabelach.

#### 2 - postulat gwarancji dostępu

Do każdej pojedynczej danej dostęp możliwy jest poprzez nazwę tabeli, nazwę kolumny oraz wartość/wartości klucza głównego.

NAZWA_BAZY_DANYCH.NAZWA_SCHEMATU.NAZWA_TABELI.NAZWA_KOLUMNY

#### 3 - postulat obiektu null

W systemie zarządzania bazą danych (SZBD) dostępny jest specjalny obiekt typu null reprezentujący stan braku wartości (tj. reprezentujący wartość brakującą, nieokreśloną lub nieznaną) - różny od każdej konkretnej wartości (jak 0 lub napis o zerowej długości) oraz niezależny od typu danych.

W SQL nie można bezpośrednio porównywać wartości do NULL, trzeba użyć **IS NULL** lub **IS NOT NULL**.

#### 4 postulat struktury metadanych

Informacje o obiektach bazy danych tworzących schemat bazy danych są na poziomie logicznym reprezentowane za pomocą tabel i dostępne tak jak każde inne dane.

#### 5 postulat pełnego języka danych

W SZBD zaimplementowany jest pełny język, obejmujący definiowanie tabel, perspektyw, więzów spójności, operowanie danymi (zarówno na poziomie interaktywnym, jak też przez interfejs programistyczny), nadawanie uprawnień użytkownikom, przeprowadzanie na bazie danych operacji pogrupowanych w transakcje.

#### 6 - postulat modyfikowania danych przez perspektywę

SZBD umożliwia modyfikowanie danych przy użyciu perspektyw w sytuacji, gdy taka modyfikacja jest semantycznie możliwa.

#### 7 - postulat modyfikowania danych na wysokim poziomie abstrakcji

SZBD umożliwia modyfikowanie danych za pomocą operacji, których argumentami są tabele (perspektywy) – a więc nie tylko w sposób nawigacyjny, polegający na przejściu wszystkich wierszy (rekordów) w tabeli (perspektywie).

#### 8 - postulat fizycznej niezależności danych

Zmiany w metodach zapisu danych i dostępu do nich nie mają wpływu na aplikację.

#### 9 - postulat logicznej niezależności danych

Zmiany w tabelach zachowujące informacje poprawne semantycznie, nie mają wpływu na aplikację.

#### 10 - postulat niezależności więzów spójności

Więzy spójności są definiowane w języku bazy danych (nie muszą być wyrażane w aplikacji).

#### 11 postulat niezależności dystrybucyjnej

SZBD (i jego język) umożliwiają używanie danych zapisanych w różnych fizycznie miejscach (w różnych węzłach sieci).

#### 12 - postulat zabezpieczenia przed operacjami na niższych poziomach abstrakcji

Jeżeli system umożliwia operacje na niższych poziomach abstrakcji, nie mogą one naruszać relacyjnego modelu danych (w tym nie mogą omijać ograniczeń określonych przez więzy spójności).

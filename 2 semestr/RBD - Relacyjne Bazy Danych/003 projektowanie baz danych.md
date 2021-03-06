# RBD

## 003 projektowanie baz danych

### Proces projektowania bazy danych

- co jest przedmiotem projektu?
- jaki jest cel projektu, jakie problemy projekt ma rozwiązać lub usprawnić działąnie rozwiązań dotychczasowych
- jakie funkcje będą realizowane w ramach projektu?
- kto te funkcje będzie wykorzystywał?
- jakie informacje (pod postacią danych) muszą być przechowywane w bazie danych, aby powyzsze założenia mogły zostać zrealizowane?
- jaki jest przewidywany aspekt ekonomiczny całego przedsięwzięcia?

### Etapy projektowania bazy danych

#### 1 Faza analizy

#### 2 Etap projektowy

#### 3 Faza implementacji i wdrożenia

### Diagram związków encji

Model, zarówno fragmentu rzeczywistości, który leży w obszarze zainteresowań systemu, jak też struktury bazy danych. Jak każdy model stanowi uproszczenie opisywanego obiektu.

#### Powinien

- w sposób jednoznaczny określać wymagania użytkowników w zakresie kompletności przechowywania w niej danych 
- umożliwiać sprawdzenie czy analityk systemu dobrze zrozumiał intencje
użytkowników i specyfikę środowiska, w którym projektowany system będzie
eksploatowany
- być istotnie prostszy od samej bazy danych, ponieważ abstrahuje on od szczegółów implementacyjnych, które muszą być później opracowane przez projektanta bazy danych tak, aby baza danych mogła powstać i spełniać postawione przed nią
zadania.

### Narzędzia CASE (Computer Aided Software Engineering)

Specjalizowane programy wspomagające procesy projektowania systemów
informacyjnych, pozwalające na tworzenie wielu rodzajów diagramów. Narzędzia **CASE** dostarczają narzędzi graficznych do projektowania i rysowania diagramów na ekranie komputera.

### Encja

Byt, coś co istnieje, jest odróżnialny od innych bytów, co da się opisać, o czym informację można poznać i przechowywać.

#### Atrybut encji

Abstrakcyjne cechy, a nie konkretne wartości. Np. atrybutem encji **Student** jest _nazwisko_. Atrybut musi opisywać encję, a nie jej związki z innymi encjami!

### Pierwsza postać normalna

Encja jest w pierwszej postaci normalnej, jeśli:
opisuje jeden typ obiektów,
- wartości atrybutów są elementarne (atomowe, niepodzielne) - każda kolumna jest
- wartością skalarną (atomową), a nie macierzą lub listą czy też czymkolwiek, co posiada własną strukturę,
- nie zawiera kolekcji (powtarzających się grup informacji),
- posiada klucz,
- kolejność atrybutów może być dowolna (znaczenie danych nie zależy od kolejności atrybutów, ich kolejność nie może kodować żadnej informacji)

Postulat atomowości można też rozumieć jako brak możliwości rozdzielenia informacji zapisanej w pojedynczej komórce tabeli albo jako jednorodność atrybutu. Np. atrybut _Dzieci pracownika_ encji **Pracownik** jest błędnym rozwiązaniem. Może co prawda służyć do zero - jedynkowego kodowania na nim.

### Klucz

Jednoznaczny identyfikator, zbiór (może być jednoelementowy) atrybutów danej encji, których wartości jednoznacznie identyfikują każdą instancję tej encji. Zbiorów atrybutów obdarzonych taką właściwością może być więcej niż jeden, ale tylko jeden z nich jest wybierany do roli **klucza głównego**.

### Wzięzy spójności (constraints)

Narzędzie **CASE** udostępniają możliwość definiowania więzów spójności na etapie tworzenia diagramu związków encji. Więzy referencyjne są definiowane automatycznie wraz ze zdefiniowaniem związków encji. Ponadto możliwe jest zdefiniowanie więzów klucza głównego, więzów **NOT NULL** oraz więzów **UNIQUE**. Na ogół możliwe jest zdefiniowanie więzów **CHECK**.

### Indeks

Wśród atrybutów encji możemy wyróżniać atrybuty, bądź grupy atrybutów, względem wartości których będą wyszukiwane egzemplarze encji. Dla takich atrybutów specyfikujemy indeksy. Indeks na kluczu głównym jest zakłądany automatycznie i nie trzeba go oddzielnie specyfikować.

### Związek

Uporządkowana lista encji. Poszczególne encje mogą na niej występować wielokrotnie. Każdy związek określa pewną zależność między zbiorami egzemplarzy (instancji) encji wchodzącymi w skłąd związku - instancję związku.

Związek można zapisać formalnie przy użyciu notacji relacyjnej:  

$Z(E_1,\  ...,\ E_n)$

Można też opisywać werbalnie.

Każdy związek ma nazwę!

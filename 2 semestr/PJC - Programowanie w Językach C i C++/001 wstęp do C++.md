# PJC

## 001 wstęp do C++

Funkcja _main_ jest punktem wejściowym, ale nie znajduje się w żadnej klasie. C++ jest językiem "hybrydowym", można pisać kod bez używania klas.

Funkcje nie muszą mieć ciała, jednak muszą znajdować się przed _main_.

### g++

#### Użycie

`g++ <nazwa_pliku>`

`-pedantic-errors` - niweluje wiele błędów, nie pozwala ukończyć kompilacji, jeżeli napotka niektóre błędy

### Preprocesor

Analizuje i zmienia kod przed jego kompilacją.

`#ifdef x` to to samo co `#if defined x`

```c++
#define x

...
...

#ifdef x
    // kod
#endif
```

W powyższym przykładzie kod zostanie wykonany tylko wtedy, kiedy _x_ będzie zdefiniowane.

### cout

Strumień wyjściowy

```c++
cout << <to co umieszczamy w strumieniu>
```

### cin

Strumień wejściowy

```c++
cin >> <to co umieszczamy w strumieniu>
```

### include

`#include <file>` - importuje bibliotekę _file_

`#include "file"` - importuje plik _file_

### Bool

W C++ każda wartość prymitywnego typu różna od zera jest równa true, a zero jest równe false.

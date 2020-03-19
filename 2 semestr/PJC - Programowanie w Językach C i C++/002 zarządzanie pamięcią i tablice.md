# PJC

## 002 zarządzanie pamięcią i tablice

### Wskaźniki

Wskaźniki przechowują adres danej zmiennej.

``` c++
double x;
double* pointerX = &x; // wskaźnik zmiennej 'x'

void* voidPointerX = pointerX; // "wskaźnik generyczny", przechowuje jedynie adres zmiennej, nie ma informacji o jej typie
```

### Referencje

Referencje odnoszą się do wartości, które są przechowywane pod danymi adresami. 

```c++
double y;
double& referenceY = y; // referencja do zmiennej 'y'
```

### Funkcje używające wskaźników i referencji

Przyjrzyjmy się poniższej funkcji:

```c++
int function(int value)
{
    return ++value;
}
```

Jest to funkcja, która przyjmuje jako argument zmienną typu **int** i zwraca tę wartość zwiększoną o **1**. Jednak z samą zmienną **value** nic się nie dzieje, pobierana jest jedynie jej wartość i jeżeli nie przypiszemy zwróconej wartości, dane przepadną.

Teraz przyjrzyjmy się drugiej funkcji:

```c++
int function(int* pointer)
{
    return ++(*pointer);
}
```

W tym przypadku argumentem jest wskaźnik i zwracana jest wartość, na którą wskazuje ten wskaźnik, zwiększoną o jeden. Rezultatem wykonania tej funkcji jest modyfikacja oryginalnej zmiennej, a nie jej kopii, jak w pierwszym przykładzie.

### Tablice

Tablice, w przeciwieństwie do Javy, nie są obiektami, a co za tym idzie, nie zawierają żadnych metod. Funkcje nie mogą zwracać tablic, jednak mogą zwracać jej adres w pamięci.

```c++
int[] arrayInt = {0, 1, 2, 3};
int arraySize = sizeof(arrayInt); // "sizeof" zwraca ilość bajtów, nie długość tablicy!

char[] arrayChar = {'B', 'a', 's', 'i', 'a', '\0'}; // '\0' w tablicy oznacza koniec napisu
```

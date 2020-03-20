# PJC

## 003 vectory, etykiety, stałe, zmienne globalne

### Macierze

Macierze to inaczej tablice dwuwymiarowe.

```c++
int array2D[3][4] = { {1, 2, 3}, {4, 5, 6, 7} };
```

Do tablicy charów można zapisywać dane podając stringa, jak w poniższym przykładzie.

```c++
char napis1[100], napis2[100];

std::cout << "Podaj dwa napisy: ";
std::cin >> napis1 >> napis2;

std::cout << "napis1: " << napis1 << std::endl;
std::cout << "napis2: " << napis2 << std::endl;
```

---

### Vectory

Odpowiednik listy. Vector jest obiektem i ma swoje metody, np. _push_back_.

```c++
vector<int> vec{2, 1}; // vector ma długość 2
vec.push_back(0); // dodajem kolejny element do vectora, który ma teraz długość 3

vec1.size() // zwraca długość vectora

for (int i = 0; i < vec.size(); i++)
{
    std::cout << vec.at(i) << std::endl; // używająć metody "at()" dostaniemy wyjątek, jeżeli wyjdziemy poza zakres, więc jest bezpieczne
    std::cout << vec[i] << std::endl; // odnosząc się bezpośrednio do elementu, w przypadku błędu nie otrzymamy wyjątku, jest mniej bezpieczne, ale szybsze
}

for (const int& element : vec) // pracujemy na oryginałach vectora, jednak użyliśmy "const", więc nie możem ich zmodyfikować
{
    std::cout << element;
}
```

W poniższym przykładzie użyte zostało _auto_ zamiast _int_. _Auto_ zmusza kompilator do "zgadnięcia" typu danej zmiennej.

```c++
for (const auto& element : vec) // pracujemy na oryginałach vectora, jednak użyliśmy "const", więc nie możem ich zmodyfikować
{
    std::cout << element;
}
```

### Aliasy

```c++
typedef long MY_INT; // od teraz "MY_INT" jest inną nazwą typu "long"

MY_INT number; // tak naprawdę zmienna "number" jest typem "long"
```

### Zakres globalny

Zmienne globalne dostępne są z każdego miejsca. Nia należy ich jednak stosować często. Powinno się ograniczyć użycie zmiennych globalnych do absolutnego minimum.

```c++
#include <iostream>

int global; // zmienna globalna

int main()
{
    int global; // zmienna lokalna

    ::global = 10; // :: oznacza wzięcie zmiennej z zakresu globalnego

    global = 5; // napisanie nazwy zmiennej bez :: oznacza wzięcie zmiennej z zakresu lokalnego
}
```

### Zmienne statyczne

```c++
int counter;

void fun()
{
    static int counter; // "static" oznacza, że tworzy się zmienna, ale nie na stosie, co za tym idzie, nie zginie
}
```

### Stałe

Stałe muszą być inicjowane od razu przy tworzeniu.

```c++
// "const" i "int" są zamienne miejscami
const int var1;
int const var2; 
```

```c++
const double PI = 3.14; // dobrze!
```

```c++
const double PI;
PI = 3.14; // źle!
```

```c++
const int i = 25;
int* pi = &i; // źle!
```

### Etykiety

Etykietowanie pozwala "skoczyć" do odpowiednich fragmentów kodu za pomocą _goto_. Rozwiązanie bardzo nieprzejrzyste i nie powinno się go stosować.

```c++
goto LABEL;

if (false)
    LABEL:if(...)
        ...
```

```c++
double a, b, c;
std::cin >> a >> b >> c;

if (auto delta = b * b - 4 * a * c; delta > 0)
    std::cout << "delta: " << << std::endl;
```

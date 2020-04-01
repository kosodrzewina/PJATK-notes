# PJC

## 004 funkcje

### Operator warunkowy

```c++
(warunek) ? jeżeli prawda : jeżeli fałsz;
```

### Kolejność wywoływania funkcji

```c++
int value = fun1(a) + fun2(b);
```

W tym przypadku nie jest określone w jakiej kolejności wywołają się funkcje.

Każda funkcja "widzi" funkcje, które są zapisane powyżej. Dobrą praktyką jest więc pisanie deklaracji funkcji przed i pisanie ich ciała po "mainie". W ten sposób nie musimy się potem martwić o kolejność zapisywania.

```c++
...
...

int fun(string argument);

int main()
{
    fun("tekst");
}

int fun(string argument)
{
    ...
    ...
}
```

### Deklaracja parametrów funkcji

Deklarowanie zmiennych funkcji jako argumentów oznacza nadawanie im domyślnej wartości.

```c++
void fun(int a, int b = 0, double x = 3.14);
```

### Inline

Modyfikator _inline_ oznacza, że kompilator nie powinien kompilować danej funkcji w standardowy sposób, tylko zastąpić jej wywołanie treścią ciała funkcji.

```c++
inline int fun(int num)
{
    return 2 * num;
}
```

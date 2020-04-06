# PJC

## 005 lambda i wskaźniki funkcji

### Wskaźniki funkcji

Tak wygląda wskaźnik do funkcji, zwracającą ```int``` i pobierającej jedną zmienną typu ```double```.

```c++
int (*pointerFun)(double);
```

Taki wskaźnik możemy zainicjować w taki sam sposób jak wskaźniki do zmiennych.

```c++
pointerFun = &fun;
```

### Lambda

Anonimowe funkcje, które można implementować lokalnie.

```c++
[domknięcie](parametry) -> typ_zwracany {ciało}
```

Użycie domknięć (może być puste):

```c++
[&, a] // weź wszystkie argumenty przez referencje, za wyjątkiem 'a'
```

---

```c++
[=, &x] // zrób kopie wszystkich argumentów, za wyjątkiem 'x', który weź przez referencję
```

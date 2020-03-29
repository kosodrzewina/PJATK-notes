# RBD

## 004 związki

### Właściwości związku - różne

- cardinality (licnzość związku)
- relationship type
- child has parent (opcjonalność związku)
- parent-to-child relationship is (wskazuje aktualne ustawienie liczności związku)

### Właściwości związku - typ

**Typ związku** _identyfikujący_ lub _nieidentyfikujący_ określa, czy do zidentyfikowanego egzemplarza (instancji) encji po stronie "wiele" konieczne jest istnienie powiązanego z nim egzemplarza encji po stronie "jeden".

### Właściwości związku - akcje referencyjne

Realizacja referencyjnych więzów integralności, czyli wymogu istnienia egzemplarza encji po stronie "jeden" związku, jeśli odwołuje się do niego egzemplarz po stronie "wiele", wymusza deklarację zachowania SZBD w sytuacji, gdy następuje próba usunięcia lub modyfikacji egzemplarza encji po stronie "jeden" związku, w którym z usuwanym egzemplarzem powiązane są egzemplarze encji po stronie "wiele".

### Związek niejednoznaczny

To taki związek, który nie jest jednoznaczny, czyli nie jest funkcją. Jeżeli mamy do czynienia z koncepcyjną zależnością pomiędzy dwiema encjami, ale nie da się ona opisać związkiem tak, jak robiliśmy to dotychczas, mówimy o związku niejednoznacznym. Definiując związek użyliśmy sformułowania "uporządkowana para encji". W przypadku związku niejednoznacznego nie jesteśmy w stanie takiej pary uporządkować, czyli wskazać poprzednika i następnika.

### Związek rekurencyjny

Jeżeli w związku jedna encja występuje wielokrotnie, mamy do czynienia ze związkiem rekurencyjnym. Przykładem może być wzajemna podległość wykładowców - jeden jest przełożonym innych. Ten typ związku nie moze być związkiem identyfikującym, musi być również związkiem opcjonalnym, czyli dopuszczać NULL jako wartość klucza obcego.

### Związek jedno-jednoznaczny

Inaczej związek jeden-do-jeden. Jest to szczególny przypadek związku jednoznacznego. Jest to taki związek jednoznaczny, którego instancja jest różnowartościową funkcją częściową 1-1. Inaczej mówiąc, każdej instancji encji po stronie "wiele" odpowiada co najwyżej jedna instancja encji po stronie "jeden".

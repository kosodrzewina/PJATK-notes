# TAK

## 003 największy wspólny dzielnik

Nie ma wzoru na największy wspólny dzielnik, który działa dla każdych dwóch liczb.

### Pierwszy pomysł na $NWD(m, n)$

Dla $0 \leqslant m \leqslant n$ oraz $n > 0$

- Jeśli $m = 0$ to $NWD(m, n) = n$
- Jeśli $m > 0$ to $NWD(m, n) = NWD(n - m, m)$

### $NWD(m, n)$ gdy $m \leqslant n$

$P$ - parzyste

- $N$ gdy $m = 0$
- $NWD(\frac{m}{2}, \frac{n}{2})$ gdy $m$ należy do $P$ i $n$ nie należy do $P$
- $NWD(\frac{m}{2}, n)$ gdy $m$ należy do $P$ i $n$ nie należy do $P$
- $NWD(m, \frac{n}{2})$ gdy $m$ nie należy do $P$ i $n$ należy do $P$
- $NWD(n - m, n)$ gdy $m$ i $n$ nie należy do $P$

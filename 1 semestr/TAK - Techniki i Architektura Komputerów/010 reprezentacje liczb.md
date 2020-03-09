# TAK

## 010 reprezentacje liczb

**LOGLAN** - obiektowy język programowania stworzony w latach 70' w Polsce

Nie ma uniwersalnego algorytmu na kodowanie liczb ujemnych. Są 3 systemy kodowania:

- Znak-moduł prosty (2-MP)

  - 0000 - 0111 (0 - 7); 1000 - 1111 ((-0) - (-7))

- Znak-moduł odwrotny (uzupełnieniowy do 1) (2-MO)

  - 0000 - 0111 (0 - 7); 1000 - 1111 ((-7) - (-0)) Podobnie jak znak-moduł prosty, tylko wartości ujemne są w odwrotnej kolejności. Zaletą tej zmiany były bardzo efektywne operacje na bitach

- Uzupełnieniowy (do dwóch) (U2)

  - 0000 - 0111 (0 - 7); 1000 - 1111 ((-8) - (-1))

Ułamki binarne  
… $2^1; 2^0$ . $2^{−1}; 2^{−2}$ …

- $\frac{1}{2} = 0.1$
- $\frac{1}{4} = 0.01$
- $\frac{3}{4} = \frac{1}{2} + \frac{1}{4} → 0.11$
- $\frac{2}{3} = 0.1010101(01)$
- $\frac{1}{10} = 0.00011001100(1100)$

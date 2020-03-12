# SOP

## 001 wstęp

asmyk - ftp, mail

### Wczesne systemy - początek lat 50-tych

- struktura
  - duże maszyny uruchamiane z konsoli
  - pojedynczy użytkownik systemu
  - programista/użytkownik jako operatorzy
- wczesne oprogramowanie
  - asemblery
  - kompilatory
  - programy ładujące
  - biblioteki
- proste systemy wsadowe
  - operator systemu komputerowego
  - użytkownik <> operator
  - redukcja czasu przygotowania zadań

### Pierwsze proste systemy operacyjne

- niska wydajność systemu - CPU o dużej szybkości musiał czekać na wykonanie powolnych operacji WE/WY
- rozwiązanie - wprowadzenie technologii dyskowej **spooling** - simultaneous peripheral operations on-line
- czyli - jednoczesna, bezpośrednia praca wykonująca się w puli zadań

### Wieloprogramowe systemy wsadowe

Jeżeli istnieje pula zadań, to możliwe jest planowanie wykonywalnych zadań (szeregowanie zadań).

### Systemy z podziałem czasu

- czas proocesora jest dzielony przez kilka zadań, które są trzymane w pamięci operacyjnej - multi tasking
- przełączanie zadań następuje bardzo szybko
- wielu użytkowników może dzielić równocześnie jeden komputer
- chroniony tryb procesora

### Systemy równoległe

- systemy wieloprocesorowe: n procesorów lub rdzeni

### Dlaczego systemy równoległe

- jakie problemy zmuszają nas do wykorzystywania komputerów równoległych
  - przewidywanie pogody

### Systemy czasu rzeczywistego

- często używane jako urządzenie kontrolne w dedykowanych aplikacjach takich jak kontrolowanie wksperymentu naukowego, wizualizacja wyników badań medycznych, w systemach kontroli przemysłowej, itp.
- dobrze zdefiniowane wymagania czasowe
- systemy czasu rzeczywistego mogą być rygorystyczne lub łagodne
- rygorystyczne systemy czasu rzeczywistego

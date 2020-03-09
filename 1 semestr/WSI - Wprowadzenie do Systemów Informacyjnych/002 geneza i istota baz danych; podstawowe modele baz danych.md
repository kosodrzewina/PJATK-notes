# WSI

## 002 geneza i istota baz danych; podstawowe modele baz danych

### Przechowywanie danych

- Gliniane tabliczki
- Papirus, pismo ręczne
- Pergamin, pismo ręczne
- Papier
- Druk
- Komputer - rewolucja w technologii

### Wymagania baz danych

- Trwałość - dane mają być przechowywane przez pewien okres czasu, na ogół nieokreślony z góry
- Zgodność z rzeczywistością - dane mają jak najbardziej opisywać rzeczywistość
- Kontrolowanie replikacji - baza musi gwarantować kontrolę nad (ewentualną) redundancją (nadmiarową informacją)
- Projektowanie struktury bazy według jednego modelu danych
- Współbieżny dostęp do danych - umożliwienie wykonywania wielu jednoczesnych operacji na danych, przy zachowaniu gwaranci poprawności danych
- Ochrona danych - zagadnienie wieloaspektowe; bezpieczeństwo danych możemy rozważać na wielu płaszczyznach i w wielu ujęciach
- Niezależność danych i wykorzystujących je procesów - właściwość mająca duży wpływ na dalszy rozwój systemu informacyjnego oraz możliwość szerokiego wykorzystania bazy danych w ramach tego systemu

### Modele baz danych

- Kartotekowy - dane przechowywane w tablicach w postaci rekordów o jednakowej strukturze. Rekordy mogą być sortowane, filtrowane. Np. arkusze w Excel lub tabele w Word.
- Hierarchiczny - dane przechowywane w postaci rekordów w układzie podrzędny - nadrzędny, tworząc strukturę drzewa. Każdy rekord ma swojego rodzica. Jeżeli rekord ma więcej niż jednego rodzica, musi być kopiowany, aby zachować powyższą regułę. Do tworzenia takiego modelu wykorzystywane są języki programowania, np. C.
- Sieciowy - stanowi rozszerzenie modelu hierarchicznego.
- Relacyjny - stanowi radykalne odejście od modeli klasycznych. Wykorzystywany np. SQL
- Obiektowy - koncepcja obiektowych baz danych powstała jako następstwo konieczności współpracy obiektowych języków programowania z nieobiektowymi strukturami danych.

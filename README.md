#[PL]

# Interfejs graficzny Ardu I/O

Interfejs graficzny Ardu I/O służy podstawowej obsłudze portów wyjść i wejść przy pomocy programu na komputery klasy PC oraz transmisji szeregowej pomiędzy komputerem a mikrokontrolerem Arduino.

Funkcje programu:
  - Obsługa jedenastu wyjść cyfrowych
    - Wśród nich 3 złączy typu PWM:
        - Podanie sygnału stałego
        - Podanie sygnału modulowanego
  - Odczyt z 6 wejść analogowych

W obecnie prezentowanej wersji złącza PWM odpowiadają za kontrolę diody RGB, natomiast do pozostałych wyjść podłączone są jednokolorowe diody.

### Wersja
1.0

### Technologia

Ardu I/O oparty jest o:

* [arduino] - platforma sprzętowa
* [python] - oprogramowanie po stronie komputera


### Instalacja

Do uruchomienia modułu konieczne jest pobranie sterowników ze strony [projektu] [ard], jak również wsparcie dla języka python.
Kody programów są umieszczone [w repozytorium GitHub][git].


### Obsługa

###### Aby uruchomić główne okno programu należy podłączyć moduł.

Główne okno programu posiada siedem przycisków:
1. Połącz/rozłącz
    * służy do otwarcia/zamknięcia połączenia między komputerem a kontrolerem z prędkością 9600 bps
2. Synchronizacja czasu
    * słuzy do synchronizacji czasu kontrolera. Domyślnie 0:00:00 1 STY 1970 
3. Dioda RGB
    * zmiana koloru diody RGB w cyklu R->G->B->OFF
4. Zapis na pin cyfrowy
    * wskazanie pinu do zmiany jego stanu
5. Sygnał modulowany
    * podanie sygnału modulowanego na wybrany port PWM; porty są od siebie niezależne
6. Ręczne ustawienie koloru diody
    * możliwość ręcznego dostosowania koloru przy pomocy trzech suwaków
7. Odczyt z pinu analogowego
    * wskazanie pinu analogowego do odczytu wartości

Polecenia wydawane poprzez interfejs są wykonywane przez kontroler. Wprowadzone komendy są wyświetlane na wbudowanym wyświetlaczu LCD.


### Rozwój

Twórcy wsparciem nie pogardzą. 
Najbliższe cele:
- poprawa jakości grafiki
- stopinowe zmniejszanie liczby błędów

#### Schemat budowy
Schemat graficzny znajduje się w [bibliotece Fritzing][frt].
##### Słowny opis wyjść:
- Piny 0,1 - zarezerwowane na transmisję szeregową
- Piny 2,3,4 - Rejestr przesuwny 74HC595
- Piny 5,6,7,8,12,13 - obsługa wyświetlacza graficznego 2X16
##### Użyte komponenty:
- Arduino UNO v3
- rejestr przesuwny 74HC595
- wyświetlacz LCD 2X16
- dioda RGB
- 8x dioda jednokolorowa
- 12x opornik 220 $$\Omega$$
- potencjometr

#### Znane błędy

 - Brak możliwości wybrania portu COM (domyślnie COM3)
 - Brak obsługi wyjątków
 - Brak automatycznej synchronizacji czasu


   [arduino]: <https://www.arduino.cc/>
   [python]: <https://www.python.org/>
   
   
   [ard]: <https://www.arduino.cc/en/Main/Software>
   [git]:  <https://github.com/Trishun/Ardu-I-O.git>
   [frt]: <http://fritzing.org/projects/ardu-io>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>



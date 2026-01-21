# Baza danych z ksiązkami – projekt w Pythonie

## Opis projektu

Projekt jest prostą aplikacją konsolową napisaną w języku Python, służącą do zarządzania bazą danych książek.  
Dane są przechowywane lokalnie w pliku bazy danych SQLite (`books.db`) przy użyciu standardowego modułu `sqlite3`.

Aplikacja nie korzysta z serwerów dużych baz danych. Cała baza zapisywana jest w jednym pliku, co spełnia wymagania zadania projektowego.

---

## Funkcjonalności

Program umożliwia wykonywanie podstawowych operacji na bazie danych:

- dodawanie książek (tytuł, autor, rok wydania),
- usuwanie książek po tytule (z informacją, gdy książka nie istnieje),
- wyszukiwanie książek po frag

---
## Wykorzystane technologie

- Python 3
- SQLite
- Moduł `sqlite3` (wbudowany w Pythona)

Program nie wymaga instalacji zewnętrznych bibliotek ani serwerów baz danych.

---

## Wymagania i instalacja

Do uruchomienia projektu wymagane jest:

- Python w wersji 3.8 lub nowszej

---

## Omówienie modułów

### `main.py`

Moduł `main.py` stanowi punkt wejścia programu.  
Odpowiada za interakcję z użytkownikiem oraz sterowanie działaniem aplikacji.

Do jego głównych zadań należą:
- wyświetlanie menu użytkownika,
- pobieranie danych wejściowych z klawiatury,
- obsługa wyborów użytkownika,
- wywoływanie odpowiednich metod z modułu `database.py`.

Moduł ten zawiera główną pętlę programu, która działa do momentu zakończenia aplikacji przez użytkownika.  

---

### `database.py`

Moduł `database.py` odpowiada za obsługę bazy danych SQLite.  
Zawiera klasę `Database`, która zarządza połączeniem z bazą danych oraz wykonuje operacje na tabelach.

Zakres odpowiedzialności modułu:
- nawiązanie połączenia z plikiem bazy danych,
- utworzenie tabeli `books`, jeśli nie istnieje,
- realizacja podstawowych operacji create, read, delete.

Zaimplementowane metody:
- `add_book()` – dodawanie nowej książki do bazy danych,
- `delete_book()` – usuwanie książki po tytule z obsługą przypadku braku rekordu,
- `search_books()` – wyszukiwanie książek po tytule lub autorze,
- `list_books()` – pobieranie wszystkich rekordów,
- `close()` – zamykanie połączenia z bazą danych.


---

### `models.py`

Moduł `models.py` definiuje model danych wykorzystywany w aplikacji.  
Zawiera klasę `Book`, która reprezentuje pojedynczą książkę w systemie.

Klasa `Book` przechowuje podstawowe informacje o książce:
- tytuł,
- autor,
- rok wydania.

Model ten umożliwia logiczne uporządkowanie danych oraz ich wygodne przekazywanie pomiędzy modułami aplikacji, zgodnie z zasadami programowania obiektowego.

---

### `books.db`

Plik `books.db` jest lokalnym plikiem bazy danych SQLite.  
Przechowuje wszystkie rekordy dodane przez użytkownika w tabeli `books`.

---

from database import Database
from models import Book


def print_menu():
    print("\nBAZA KSIĄZEK")
    print("1. Dodaj ksiązkę")
    print("2. Usuń ksiąkę")
    print("3. Szukaj ksiązki")
    print("4. Wypisz wszytko")
    print("5. Wyjdz")


def main():
    db = Database()

    while True:
        print_menu()
        choice = input("Wybierz opcje: ")

        if choice == "1":
            title = input("Tytuł: ")
            author = input("Autor: ")
            year = input("Rok: ")

            if not year.isdigit():
                print("Rok musi być liczbą!")
                continue

            book = Book(title, author, int(year))
            db.add_book(book)
            print("Ksiąka dodana.")

        elif choice == "2":
            title = input("Wpisz tytuł do usunięcia: ")
            success = db.delete_book(title)

            if success:
                print("Ksiązka usunięta.")
            else:
                print("Ksiązka nie znaleziona.")


        elif choice == "3":
            books = db.list_books()
            if not books:
                print("Baza pusta.")
            else:
                keyword = input("Wpisz szukane slowo: ")
                results = db.search_books(keyword)
                

                
                if not results:
                    print("Nie znaleziono.")
                else:
                    for title, author, year in results:
                        print(f"{title} | {author} | {year}")

        elif choice == "4":
            books = db.list_books()

            if not books:
                print("Baza pusta.")
            else:
                for title, author, year in books:
                    print(f"{title} | {author} | {year}")

        elif choice == "5":
            db.close()
            print("bye")
            break

        else:
            print("Zły input!")


if __name__ == "__main__":
    main()

#poprawa w usuwaniu ksiązek
import os
from book_data import load_books, save_books
from add_book import add_book
from view_books import view_books
from remove_book import remove_book
from search_book import search_book

def main_menu():
    while True:
        print("\n--- Book Store Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            remove_book()
        elif choice == '5':
            print("Saving data and exiting...")
            save_books()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if not os.path.exists('books.txt'):
        with open('books.txt', 'w') as f:
            pass
    
    load_books()
    main_menu()
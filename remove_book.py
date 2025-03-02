from book_data import books

def remove_book():
    isbn = input("Enter the ISBN of the book to remove: ")
    for book in books:
        if book['isbn'] == isbn:
            books.remove(book)
            print("Book removed successfully.")
            return
    print("Error: Book not found.")
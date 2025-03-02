from book_data import books

def view_books():
    if not books:
        print("No books available.")
        return

    print("\n--- List of Books ---")
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Genre: {book['genre']}, Price: {book['price']}, Quantity: {book['quantity']}")
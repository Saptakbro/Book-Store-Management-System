from book_data import books

def search_book():
    search_term = input("Enter book title or author to search: ")
    found_books = [book for book in books if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()]

    if not found_books:
        print("No matching books found.")
        return
    
    print("\n--- Search Results ---")
    for book in found_books:
        print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Genre: {book['genre']}, Price: {book['price']}, Quantity: {book['quantity']}")
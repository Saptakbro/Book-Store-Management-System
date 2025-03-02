from book_data import books

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    genre = input("Enter genre: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity in stock: "))

    # Prevent duplicate books
    if any(book['isbn'] == isbn for book in books):
        print("Error: Book with this ISBN already exists.")
        return

    books.append({
        'title': title,
        'author': author,
        'isbn': isbn,
        'genre': genre,
        'price': price,
        'quantity': quantity
    })
    print("Book added successfully.")
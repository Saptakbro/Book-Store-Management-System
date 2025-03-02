books = []

def load_books():
    global books
    with open('books.txt', 'r') as f:
        for line in f:
            title, author, isbn, genre, price, quantity = line.strip().split(',')
            books.append({
                'title': title,
                'author': author,
                'isbn': isbn,
                'genre': genre,
                'price': float(price),
                'quantity': int(quantity)
            })

def save_books():
    with open('books.txt', 'w') as f:
        for book in books:
            f.write(f"{book['title']},{book['author']},{book['isbn']},{book['genre']},{book['price']},{book['quantity']}\n")
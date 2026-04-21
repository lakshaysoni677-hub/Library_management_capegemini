from utils import books

def add_book():
    book_name = input("enter book name to be added: ").strip().upper()
    books.append(book_name)
    print((f"book - {book_name} added successfully."))

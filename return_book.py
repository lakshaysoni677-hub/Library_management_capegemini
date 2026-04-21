from utils import books, issued_books

def return_book():
    if len(issued_books)==0:
        print("No book issued earlier")
    else:
        book_name = input("enter book to be issued: ").strip().upper()
        if book_name in books:
            books.remove(book_name)
            books.append(book_name)
            print(f"book - {book_name} returned successfully.")
        else: print("")    
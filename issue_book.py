from utils import books, issued_books

def issue_book():
    if len(books)==0:
        print("No book available!!")
    else:
        book_name = input("enter book to be issued: ").strip().upper()
        if book_name in books:
            books.remove(book_name)
            issued_books.append(book_name)
            print(f"book - {book_name} issued successfully.")
        else: print("No such book available")    
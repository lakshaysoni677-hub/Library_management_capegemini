from utils import books

def show_book():
    if len(books) == 0: print("No book available")
    else:
        print("Available book:")
        for _ in books:
            print(_)
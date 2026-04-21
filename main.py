from add_book import add_book
from return_book import return_book
from issue_book import issue_book
from show_book import show_book

def library():
 while True:
    print("\n1. Add books")
    print("\n2. Show books")
    print("\n3. Issue books")
    print("\n4. Return books")
    print("\n5. Exit")

    choice = input ("enter your choice:")
    if choice.isdigit():
        choice=int(choice)
        if choice == 1: add_book()
        elif choice == 2: show_book()
        elif choice == 3: issue_book()
        elif choice == 4: return_book()
        elif choice == 5:
            print("thank you")
            break
    else:   print("invalid input!!!")
library()
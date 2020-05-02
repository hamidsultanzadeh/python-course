book_list = list()

menu = """
[1] Add book
[2] Remove book
[3] Show books
[4] Search book
[Q] - [q] Exit
"""


def add_book(book:tuple):
    book_list.append(book)


def remove_book(book:tuple):
    if book in book_list:
        book_list.remove(book)


def search_book(book:tuple):
    if book in book_list:
        return book_list.index(book)
    return -1


def show_books():
    for idx, book in enumerate(book_list):
        print("{} - {}".format(idx+1, book))


while True:
    print(menu)
    choice = input("Select : ")

    if choice == "1":
        name_book = input("Type name book: ")
        name_author = input("Type name author: ")
        add_book((name_book,name_author))
    elif choice == "2":
        name_book = input("Type name book: ")
        name_author = input("Type name author: ")
        remove_book((name_book,name_author))
    elif choice == "3":
        show_books()
    elif choice == "4":
        name_book = input("Type name book: ")
        name_author = input("Type name author: ")
        result = search_book((name_book,name_author)) + 1
        print("Index of book :", result if result != 0 else "Does not exist")
    elif choice == "Q" or choice == "q":
        print("Shutting down...")
        quit()
    else:
        print("Wrong operation. Try again")


book_list = list()

menu = """
[1] Add book
[2] Remove book
[3] Show books
[4] Search book
[Q] - [q] Exit
"""


def add_book(nm):
    book_list.append(nm)


def remove_book(nm):
    pass


def search_book(nm):
    if nm in book_list:
        return book_list.index(nm)
    return -1


def show_books():
    for idx, book in enumerate(book_list):
        print("{} - {}".format(idx+1, book))


while True:
    print(menu)
    choice = input("Select : ")

    if choice == "1":
        name = input("Type name : ")
        add_book(name)
    elif choice == "2":
        print('coming')
    elif choice == "3":
        show_books()
    elif choice == "4":
        name = input("Type name : ")
        result = search_book(name) + 1
        print("Index of book :", result if result != 0 else "Does not exist")
    elif choice == "Q" or choice == "q":
        print("Shutting down...")
        quit()
    else:
        print("Wrong operation. Try again")





import modules.booksModule as booksModule

menu_promt: str = """Please select option:
- 'a': to add
- 's': to show store
- 'd': to delete
- 'f': to search
- 'q': to quit
"""

booksModule.create_books_file()

def menu() -> None:
    user_option: str = input(menu_promt).strip().lower()

    if user_option == 'q': listener()

    if user_option == 'a':
        booksModule.add()
    elif user_option == 'd':
        booksModule.remove()
    elif user_option == 's':
        books = booksModule.getBooks()

        if books:
            booksModule.show(booksModule.getBooks())
    elif user_option == 'f':
        matched = booksModule.find_book()

        if len(matched) > 0:
            print('Matched books: ')
            booksModule.show(matched)
        else:
            print('Nothing found.')


def listener() -> None:
    start_or_stop: str = input('Press "Y" to start or "N" to stop: ').lower()

    if start_or_stop == 'y':
        menu()
    else: 
        print('Close the app.')
        return

listener()

    
menu_promt = """Please select option:
- 'a': to add
- 's': to show store
- 'd': to delete
- 'f': to search
- 'q': to quit
"""

def clear_books():
    try:
        with open('files/books.csv', 'w') as file:
            file.write('title,author,release')
    except FileNotFoundError:
        print('Not found.')

def getBooks():
    books = []

    try:
        with open('files/books.csv', 'r') as file_books:
            books_content = file_books.readlines()
            if len(books_content) <= 0:
                print('Books are empty.')
            else:
                for book in books_content[1:]:

                    title, author, release = book.strip().split(',')

                    bookDict = dict(
                      title=title,
                      author=author,
                      release=release
                    )

                    books.append(bookDict)
        return books
    except FileNotFoundError:
        print('Not found')


def add():
    title = input('Title: ').strip().title()
    author = input('Author: ').strip().title()
    year = int(input('Release year: ').strip())

    with open('files/books.csv', 'a') as books_file:
        books_file.write(f'{title},{author},{year}\n')
        print('Adding...')

def remove():
    stored_books = getBooks()

    for i, book in enumerate(stored_books):
      print(i, book.get('title'))

    user_index = int(input('Please select book index: ').strip())

    for i, book in enumerate(stored_books):
        if user_index == i:
            stored_books.pop(i)

    clear_books()

    with open('files/books.csv', 'a') as books_file:
        for book in stored_books:
            title = book.get('title')
            author = book.get('author')
            year = book.get('release')

            books_file.write(f'{title},{author},{year}\n')


def show(books = getBooks()):
    if len(books) <= 0:
        print('Store is empty.')

    for book in books:
        title = book.get('title')
        author = book.get('author')
        year = book.get('release')
        
        print(f'{title} by {author} in {year}')

def find_book():
    stored_books = getBooks()
    finded_books = []

    search_term = input('Search for book title: ').strip().lower()

    for book in stored_books:
        if search_term in book['title'].lower():
            finded_books.append(book)


    return finded_books

def menu():
    user_option = input(menu_promt).strip().lower()

    if user_option == 'q': listener()

    if user_option == 'a':
        add()
    elif user_option == 'd':
        remove()
    elif user_option == 's':
        show()
    elif user_option == 'f':
        matched = find_book()

        if len(matched) > 0:
            print('Matched books: ')
            show(matched)
        else:
            print('Nothing found.')


def listener():
    start_or_stop = input('Press "Y" to start or "N" to stop: ').lower()

    while start_or_stop != 'n':
        menu()
    else: 
        print('Close thea app.')

listener()


    
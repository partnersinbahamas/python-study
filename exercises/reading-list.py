import json

# json.load: (file, ...) => py dict
# json.dump: (file) => json

menu_promt = """Please select option:
- 'a': to add
- 's': to show store
- 'd': to delete
- 'f': to search
- 'q': to quit
"""

def create_books_file():
    try:
        initial_books = [
            dict(
                title="Design Patterns. Elements Of Reusable Object-Oriented Software",
                author="Gang Of Four",
                release="1994",
            ),
            dict(
                title="Charlie And The Chocolate Factory",
                author="Alfred A. Knopf",
                release="1964",
            ),
        ]
        with open('files/books.json', 'x') as books:
            json.dump(initial_books, books)
    except FileExistsError:
        pass

create_books_file()

def clear_books(): updateBooks([])

def getBooks():
    with open('files/books.json', 'r') as books_file:
        books_content = json.load(books_file)
        if len(books_content) <= 0:
            print('Books are empty.')
        else:
            return books_content
        
def updateBooks(data):
    with open('files/books.json', 'w') as books_file:
        json.dump(data, books_file)

def add():
    title = input('Title: ').strip().title()
    author = input('Author: ').strip().title()
    year = int(input('Release year: ').strip())

    books = getBooks()

    books.append(
      dict(
        title=title,
        author=author,
        release=year,
      ),
    )

    updateBooks(books)

def remove():
    books = getBooks()

    for i, book in enumerate(books):
      print(i, book.get('title'))

    user_index = int(input('Please select book index: ').strip())

    for i, book in enumerate(books):
        if user_index == i:
            books.pop(i)

    updateBooks(books)


def show(books):
    if len(books) <= 0:
        print('Store is empty.')

    for book in books:        
        print('{title} by {author} in {release}'.format(**book))

def find_book():
    books = getBooks()
    matched_books = []

    search_term = input('Search for book title: ').strip().lower()

    for book in books:
        if search_term in book['title'].lower():
            matched_books.append(book)

    return matched_books

def menu():
    user_option = input(menu_promt).strip().lower()

    if user_option == 'q': listener()

    if user_option == 'a':
        add()
    elif user_option == 'd':
        remove()
    elif user_option == 's':
        show(getBooks())
    elif user_option == 'f':
        matched = find_book()

        if len(matched) > 0:
            print('Matched books: ')
            show(matched)
        else:
            print('Nothing found.')


def listener():
    start_or_stop = input('Press "Y" to start or "N" to stop: ').lower()

    if start_or_stop == 'y':
        menu()
    else: 
        print('Close the app.')
        return

listener()

    
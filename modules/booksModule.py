import json
from typing import TypedDict, Union, Optional

# json.load: (file, ...) => py dict
# json.dump: (file) => json

print('ksdgjfbjdfshfb')

class Book(TypedDict):
    title: str
    author: str
    release: str

def create_books_file() -> None:
    try:
        initial_books: list[Book] = [
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

def getBooks() -> Optional[list[Book]]:
    with open('files/books.json', 'r') as books_file:
        books_content: list[Book] = json.load(books_file)
        if len(books_content) <= 0:
            print('Books are empty.')
            return None
        else:
            return books_content

def updateBooks(data: list[Book]):
    with open('files/books.json', 'w') as books_file:
        json.dump(data, books_file)

def clear_books(): updateBooks([])


# Books interaction

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


def show(books: list[Book]) -> None:
    if len(books) <= 0:
        print('Store is empty.')

    for book in books:        
        print('{title} by {author} in {release}'.format(**book))

def find_book() -> Union[list[Book], None]:
    books = getBooks()
    matched_books = []

    search_term = input('Search for book title: ').strip().lower()

    if not books: return None
    
    for book in books:
        if search_term in book['title'].lower():
            matched_books.append(book)

    return matched_books
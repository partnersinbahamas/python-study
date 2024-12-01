# Exercises
# 1. Make a decorator which calls a given function twice. You can assume the functions don't return anything important, but they may take arguments.
# 2. Imagine you have a list called books, which several functions in your application interact with. Write a decorator which causes your functions to run only if books is not empty.
# 3. Write a decorator called printer which causes any decorated function to print their return values. If the return value of a given function is None, printer should do nothing.

from typing import Callable
from functools import wraps
from modules.booksModule import getBooks

# 1
def twiced(func: Callable) -> Callable:
    @wraps(func)
    def inner():
        for i in range(2):
            print(i + 1)
            func()
    return inner

@twiced
def mockedBooksCall():
    print('Calculation...')
    print('Books: []')
    print('Exit.')

mockedBooksCall()

# 2
def chech_books(func: Callable) -> Callable:
    @wraps(func)
    def inner(books):
        if books and len(books):
            func(books)
        else:
            print(f'Function {func.__name__} was interuppted, becase books are empty.')
    return inner
      
@chech_books
def showBooks(books):
    print('-' * 10)
    for book in books:
        title = book['title']
        print(title)

def withBooks():
  books = getBooks()
  showBooks(books)
  showBooks([])

withBooks()

# 3
def printer(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args):
        callback = func(*args)
        if callback:
            print(f'Printer: {callback}.')
        else:
            print('Printer: do nothing.')
    return inner

@printer
def add(a, b):
    return a + b
@printer
def Noned(): return None

add(1, 2)
Noned()





from collections import namedtuple, defaultdict
from functools import partial

Book = namedtuple('Book', ['title', 'author', 'year'])

book = Book('Book-name', 'Book-author', 'Book-release')

# or
# _make here works as *
# book = Book._make(['Book-name', 'Book-author', 'Book-release'])

print(book)

def exponent(base, exp):
    return base ** exp

# The partial function is a way to create a new version of a function, where some portion of the arguments are already given.
square = partial(exponent, exp=2)
cube = partial(exponent, exp=3)

print(square(4))
print(cube(4))

User = namedtuple('User', ['name', 'age'])

# defaultdict allow us set to the dict some lambda func witch is calls whenever user can not be define.
users = defaultdict(
    lambda: 'User can not be defined.',
    {
        '001': User('Denys', 20),
        '002': User('Danilo', 20),
        '003': User('Denys', 20),
    }
)

user_id = input('User id: ')

print(users[user_id])
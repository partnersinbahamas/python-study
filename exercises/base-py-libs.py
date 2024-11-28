from collections import namedtuple, defaultdict
from functools import partial
from operator import mul

# Exercises
# 1. Define a Movie tuple using namedtuple that accepts a title, a director, a release year, and a budget. Prompt the user to provide information for each of these fields and create an instance of the Movie tuple you defined.
# 2. Use a defaultdict to store a count for each character that appears in a given string. Print the most common character in this dictionary.
# 3. Use the mul function in the operator module to create a partial called double that always provides 2 as the first argument.
# 4. Create a read function using a partial that opens a file in read ("r") mode.

def fill_movie():
    Movie = namedtuple('Movie', ['title', 'director', 'year', 'budget'])

    title = str(input('Movie title: '))
    director = str(input('Movie director: '))
    year = int(input('Movie year: '))
    budget = int(input('Movie budget: '))

    movie = Movie(title, director, year, budget)

    return movie

print(fill_movie())

def most_char(string):
    inventory = defaultdict(int)

    max = 0
    maxChar = ''

    for char in string:
        inventory[char] += 1

    for key, value in inventory.items():
        if value > max:
            max = value
            maxChar = key

    return maxChar

print(most_char('aaabbbbbbbv'))

double = partial(mul, 2)
print(double(3))

read = partial(open, mode='r')
with read('files/errors.txt') as r:
    print(r.read())

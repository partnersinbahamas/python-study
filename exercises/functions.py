# Exercises

# 1. Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.
# When orders matters for an operation, the first argument should be treated as the left operand, and the second argument should be treated as the right operand. For example, if the user passes in 6 and 2 to subtract, the result should be 4, not -4.
# You should also make sure that the user can’t pass in 0 as the second argument for divide. If the user provides 0, you should print a warning instead of calculating their division.

# 2. Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show. For example:
# The print_show_info function should print the information stored in the dictionary, in a nice way. For example:
#  Breaking Bad (2008) - 5 seasons
# Remember you must define your function before calling it!

# 3) Below you’ll find a list containing details about multiple TV series.
# Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for each iteration, passing in each dictionary. You should end up with each series printed in the appropriate format.

# 4) Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.
# In the day 7 project, we saw a number of ways to reverse a sequence, and you can use this to verify whether a string is the same backwards as it is in its original order. You can also use a slicing approach. Once you’ve found whether or not a word is a palindrome, you should print the result to the user.
# Make sure to clean up the argument provided to the function. We should be stripping whitespace from both ends of the string, and we should convert it all to the same case, just in case we’re dealing with a name, like “Hannah”.


tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]

def add(n1, n2):
    return n1 + n2

print('Add: ', add(1, 2))

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print('Argument cannot be zero.')

print(f'Divide: {divide(1, 2)}')
print(f'Divide on Zero: {divide(1, 0)}')

def substract(n1, n2):
    return n1 - n2

print(f'Substract: {substract(2, 1)}')

def multiply(n1, n2):
    return n1 * n2



def tv_info(shows):
    print(isinstance(shows, dict))
    if (len(shows) == 0):
        print('No gived shows')
    elif isinstance(shows, dict): # check instance
        title, seasons, release = shows.values()
        return f'{title} ({release}) - {seasons} seasons'
    else:
        for show in shows:
            title, seasons, release = dict(show).values()
            print(f'{title} ({release}) - {seasons} seasons')

def print_tv_shows(shows):
    print(tv_info(shows))

print_tv_shows(tv_show)

def is_palindrom(word):
    word = word.strip().lower()
    reversed_word = word[::-1]

    return reversed_word == word

    # or
    # t_list = list(word)
    # t_list.reverse()
    # return ''.join(t_list) == word

print(is_palindrom('hah'))
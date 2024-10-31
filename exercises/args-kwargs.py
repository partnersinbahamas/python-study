# Exercises
# 1. Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. Remember that we can use the sum function to add the values in an iterable.
# 2. Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.
# 3. Print the following dictionary using the format method and ** unpacking.
# 4. Using * unpacking and range, print the numbers 1 to 20, separated by commas. You will have to provide an argument for print function's sep parameter for this exercise.
# 5. Modify your code from exercise 4 so that each number prints on a different line. You can only use a single print call.

country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

def get_sum(*numbers):
    return sum(numbers)

print(get_sum(1, 2, 3, 4, 5))

def get_info(*args, **kwargs):
    args = (repr(arg) for arg in args)
    kwargs = (f'{key}={value}' for key, value in kwargs.items())

    print(f"Giver args: ", ', '.join(args))
    print(f"Giver kwargs: ", ', '.join(kwargs))

get_info(1, 2, 'Some.txt', False, **country)


def get_counry_info(country):
    print('In {name}, {capital} lives {population} of peopel, and the pay with {currency} currency. '.format(**country))

get_counry_info(country)


print(*range(1, 21), sep=", \n")
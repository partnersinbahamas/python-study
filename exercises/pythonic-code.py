import string as strModule
import random
# Exercises

# 1. Write a function that prompts the user for their name and then greets them. You should process the string by removing any whitespace and converting the string to title case.
# If after processing the string you're left with an empty string, the function should replace the empty string with "World" in the output.

# 2. Write a function to determine whether or not a string contains exclusively ASCII letters (a to z in either upper or lowercase).
# Hint: You should look at the constants in the string module. Documentation can be found here.

# 3.Use the sample function in the random module to create three lists, each containing fifteen numbers from 1 to 100 (inclusive). Sort each of these lists into descending order (largest first), and then truncate each list so that only 5 items remain in each.

def greeting():
    prompt = "Hello {}!"
    user_name = input('Please, enter your name: ').strip().title() or 'World'
    return prompt.format(user_name)

print(greeting())

def ascii_check(string=''):
    use_string = string

    if not string:
        use_string = str(input('Enter any string: '))

    for char in use_string:
        if char in strModule.ascii_letters:
            return f'{char} in {strModule.ascii_letters}'
        
    # or return all(char in ascii_letters for char in use_string)

    return 'String not include ASCII letters'

print(ascii_check())

def get_random_lists(count, length):
    lists = [random.sample(range(1, 101), length) for _ in range(count)]
    promt = 'List index: {} has items {}.'

    for i, n_list in enumerate(lists):
        n_list.sort()
        del n_list[:10]
        print(promt.format(i + 1, ', '.join(str(n) for n in n_list)))

get_random_lists(3, 15)






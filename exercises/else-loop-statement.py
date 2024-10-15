# Exercises
    # Congratulations on completing the first week!
    # Hopefully this wasn't too difficult, but if you're having trouble with some of the concepts, the exercises below should help solidify everything. If you get stuck, we're always around to help on our Discord server, so feel free to drop by and ask any questions.
    # 1. Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.
    # 2. Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
    # Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.
    # 3. Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.

import random;

def guessGame():
    guess = random.randint(0, 100)
    user_num = None

    print(guess)

    while user_num != guess:
        user_num = int(input('Try to guess number from 0 til 100: '))

        if (user_num > guess):
            print('Less!')
        else:
            print('More!')
    else:
        print(f'Congratulations you guessed the {guess} number.')

guessGame()

for char in 'Python':
    if (char == 'o'):
        continue
    else:
        print(char)

for n in range(1, 101):
    if n % 2 == 0:
        continue
    print(n)
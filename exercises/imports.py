# Exercises
# 1. Import the fractions module and create a Fraction from the float 2.25. You can find information on how to create fractions in the documentation.
# 2. Import only the fsum function from the math module and use it to find the sum of the following series of floats:
# 3. Import the random module using an alias, and find a random number between 1 and 100 using the randint function. You can find documentation for this function here.
# 4. Use the randint function from the exercise above to create a new version of the guessing game we made in day 8. This time the program should generate a random number, and you should tell the user whether their guess was too high, or too low, until they get the right number.

# You can find our solutions to the exercises here.

import fractions
from math import fsum
import random as rand

frac = fractions.Fraction(2.25)
print(frac)

numbers = fsum([1.43, 1.1, 5.32, 87.032, 0.2, 23.4])
print(numbers)


def randomize():
    tries = 3
    used_tries = 0

    randommed = rand.randint(1, 10)

    isExit = False

    def tryAgain():
        again = input('Try again? Y - yes, N - no: ')

        if again.lower() == 'y':
            randomize()
        else: 
            return
     
    while(not isExit):
      if used_tries >= tries:
        print('Your used all tries, please try again later.')
        print(f'Number was: {randommed}')
        used_tries = 0
        isExit = True

        tryAgain()
      else:
        used_tries += 1
        user_input = int(input('Try to gues number from 1 to 10: '))

        if user_input > randommed:
            print(f'To high. Tries: {tries - used_tries}')
        elif user_input < randommed:
            print(f'To less. Tries: {tries - used_tries}')
        else:
            print(f'You won. Guessed number: {randommed}')
            isExit = True
            tryAgain()

randomize()
# Python FizzBuzz

def fizzBuzz(numRange = 100):
    for num in range(1, numRange + 1):
        if (num / 3).is_integer():
            if (num / 5).is_integer():
                print('Fizz Buzz')
            else:
                print('Fizz')
        elif (num / 5).is_integer():
            print('Buzz')

        else:
            print(num)

fizzBuzz()

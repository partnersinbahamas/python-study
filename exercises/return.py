# Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.
# 2. Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.
# 3. Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. The data should be in the following format:
# You can choose whatever key names you like for the dictionary.
# 4. Write a function that takes in a single number and returns True or False depending on whether or not the number is prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.

def exponentiate(n1, n2):
    return pow(n1, n2)

power = exponentiate(2, 3)
print('power: ', power)

def processString(str: str):
    return str.lower().strip()

string = processString('HeLLo WorlD!  ')
print(string)

def tuppleToDict(tupl):
    actor, lang, age = tupl
    
    return dict(
        name=actor,
        came_from=lang,
        age=age
    )

dct = tuppleToDict(("Tom Hardy", "English", 42))

print(dct)

def returnBool(n):
    return not not n

print(returnBool(0))
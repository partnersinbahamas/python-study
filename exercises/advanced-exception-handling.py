


# The exception hierarchy

# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning

# -------------------------------

# Exercises
# 1. Ask the user for an integer between 1 and 10 (inclusive). If the number they give is outside of the specified range, raise a ValueError and inform them that their choice was invalid.

# 2. Below you'll find a divide function. Write exception handling so that we catch ZeroDivisionError exceptions, TypeError exceptions, and other kinds of ArithmeticError.

# 3. Below you'll find an itemgetter function that takes in a collection, and either a key or index. Catch any instances of KeyError or IndexError, and write the exception to a file called log.txt, along with the arguments that caused this issue. Once you have written to the log file, reraise the original exception.


def logger(err, func, **kwargs):
    with open('files/errors.txt', 'a') as file:
        file.write(f'Error found in {func} with values: {kwargs.items()} func as: {err}\n')

def itemgetter(collection, identifier):
    try:
        return collection[identifier]
    except (IndexError, KeyError) as err:
        logger(err, 'itemgetter', collection=collection, identifier=identifier)
        raise err
        
itemgetter([], 1)

def type_integer():
    integer = int(input('Please enter an integer between 1 and 10: '))

    if integer in range(0, 11):
        return f'Selected integer is: {integer}'
    else:
        raise ValueError(f'{integer} is not in range.')

user_integer = type_integer()
print(user_integer)


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError('Can not divide on zero') from ArithmeticError

print(divide(1, 0))

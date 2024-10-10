number = 10
del number # delete number
# print(number) => error cause we have deleted this var

number = 1 # int
digit = 17.032004 # float
string = 'Hello string' # str
boolean = True # bool 

print('number: ', number)
print('string: ', string)
print('digit: ', digit)
print('boolean: ', boolean)

numAsStr = str('5') # str to int
strAsNum = int(5) # int to str
strAsBool = bool('is it bool?')
numAsBool = bool(0) # num to True / False
intAsFloat = float(1) # int to float

print('bool casting: ',strAsBool, numAsBool)
print('int as float: ', intAsFloat)
print(numAsStr, strAsNum)

# input
x = int(input('Enter X:')) # after enter input returns str, so we need to casting to it int
y = int(input('Enter Y:'))

print('Calculation "+" answear', x + y, sep=': ')
print('Calculation "-" answear', x - y, sep=': ')
print('Calculation "*" answear', x * y, sep=': ')
print('Calculation "/" answear', x / y, sep=': ')
print('Calculation "**" answear', pow(x, y), sep=': ')

print('?: ', 'Hi' * 2) # ? yes, it will works => HiHi

# if we change data type for the same var
# inside py engine it works so:
# firtly we delete the str 'test' var using del
# and the create a new one int 'test' var
test = 'test string'

test = 10
test2 = 10

# func id returns uniq series of number witch an address that references a location in memory.
print('1: ', id(test), id(test2)) # True because Python optimizes small integers

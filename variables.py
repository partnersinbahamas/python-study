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

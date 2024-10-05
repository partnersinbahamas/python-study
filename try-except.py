# try-except | Исколючение -> used when an error occurs so that the program does not stop working
# is like trycatch in JavaScript

def userEnterValue():
  numX = None
  numY = None

  while(numY == None and numY == None):
    try:
        numX = int(input('Enter X:'))
        numY = int(input('Enter Y:'))

        return numX + numY
    except ValueError: # error key
        print('Invalid value. Try again.')

print(userEnterValue())
 
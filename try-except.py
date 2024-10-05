# try-except | Исколючение -> used when an error occurs so that the program does not stop working
# is like trycatch in JavaScript

def userEnterValue():
  try:
    numX = int(input('Enter X:'))
    numY = int(input('Enter X:'))

    return numX + numY
  except ValueError: # error key
    return 'Invalid value. Try again.'

print(userEnterValue())
 
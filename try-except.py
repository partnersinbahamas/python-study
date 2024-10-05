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
    # you can handle multiple errors in a row
    except ZeroDivisionError:
        print('Zero division allowed. Try again.')
    # else calls if no error handler was called or was called try block
    else:
        print('Else')
    finally:
       print('Finally done')

print(userEnterValue())
 
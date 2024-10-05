# with as -> works with files

# Expample w/0 with as
try:
    file = open('text.txt', 'r') # open read, file not exist
    content = file.read()
except FileNotFoundError:
    print('File not found.')
finally:
    # at the end we need to close our file
    # but its not working cause file was created in another scope
    # to make it wotks as expected, we need with as
    # file.close()
    print('Finally')


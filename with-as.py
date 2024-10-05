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

# Expample with as
def readFile(path):
    try:
        # with as opens file and late close it by themself
        with open(path, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('File not found.')

readFile('files/pytext.txt')
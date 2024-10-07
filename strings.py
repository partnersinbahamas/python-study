# you can use most of list methods for string

string = 'Python !!'
length = len(string)
markCount = string.count('!')

print(string, length, markCount, string)

print('-----')

# strings only methods

upperCase = string.upper()
lowerCase = string.lower()
isUpper = upperCase.isupper() # returns true if each char in upper case
isLover = lowerCase.islower() # returns true if each char in lower case

capitalized = lowerCase.capitalize() # make first char of string to upper case
findPy = string.lower().find('py') # (string) returns finded index of first string char

stripped = ' Hello!  '.strip() # remove spaces
titled = 'DENYS BOKOV'.title() # make capitalize for first letter in each word: DENYS BOKOV => Denys Bokov

print('stripped', stripped)
print('upper: ', upperCase, isUpper)
print('lower: ', lowerCase, isLover)
print('capitalize:', lowerCase, string, ': ', capitalized)
print('find py: ', findPy)

print('-----')

langs = 'python, javaScript, c++'
splitLangs = langs.split(', ')

for index in range(len(splitLangs)):
    # not works if save splitLangs[index] into variable
    splitLangs[index] = splitLangs[index].capitalize()
    
langsCapitalize = ' | '.join(splitLangs)

print(langs, splitLangs, langsCapitalize)

# steps | срезы
# steps work same for list, tuples etc..

word = 'Porsche'
print(word[0::2]) # (from:to = -1:step = 1) => sche
print(word[1::2]) # (from:to = -1:step = 1) => sche
print(word[::-1]) # reverse string
print(word[:4:]) # until 4th index

# The placeholders for our values are {}
# you can set index inside {} like {0}, {1}
# or names line {name}, {age}
# use f'' to write message with variable

messagesWithIndex = 'Hi! My name is {0} and am {1} years old. {0} works as a {2}'
messageWithWords = 'Hi! My name is {name} and am {age} years old. {name} works as a {work}'

formattedIndex = messagesWithIndex.format('Denys', 20, 'Frontend developer') # (index: 0, 1, 2)
formattedWords = messageWithWords.format(name='Denys', age=20, work='Frontend developer') # (word: name, age, work)

print('message: ', messagesWithIndex, messageWithWords)
print('messages With Index: ', formattedIndex)
print('message With Words: ', formattedWords)

city = "Berlin"
print(f'I live in {city}')
print(f'{100.0000:.2f}') #:.(numer)f => numbers after comma => 100.0000 => 10.00
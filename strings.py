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
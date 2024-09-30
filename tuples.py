
# IMPORTANT: to create tuple use: (element,) | element, | (element, element) | element, element
# Hint:
    # has most of methods from lists(arrays) 
    # tuples similar with lists(arrays),
    # wokrs as a constant value
    # has less weight as a list

# if one element in tuple, its became to 5 as number
# to make it tuple add more elements, or comma at the end => (5,)
testTuple = (5)
print('testTuple: ', testTuple)

tuple = ('string', 1, True) # creates with () or just: 'string', 1, True
lastOfTuple = tuple[-1]
# tuple[0] = 'change tuple' # error => tuple is constat
print('tuple: ', tuple, lastOfTuple)

print('----- tuples in loops')

for tupleEl in tuple:
    print('element: ', tupleEl)
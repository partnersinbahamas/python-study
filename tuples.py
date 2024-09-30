
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

tupleData = ('string', 1, True) # creates with () or just: 'string', 1, True
lastOfTuple = tupleData[-1]
# tuple[0] = 'change tuple' # error => tuple is constat
print('tupleData: ', tupleData, lastOfTuple)

print('----- tuples in loops')

for tupleEl in tupleData:
    print('element: ', tupleEl)

print('-----')

nums = [1, 2, 3, 4, 5]
numsTuple = tuple(nums) # reverse list to tuple
stringTuple = tuple('lern Phython')
print('list: ', nums, 'tuple: ', numsTuple)
print('stringTuple: ', stringTuple)
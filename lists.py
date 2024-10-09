list = [1, 2, 3, 4, 5, [6, 7]]
list[0] = 10
del list[3] # delete element with index 3
lastElement = list[-1][-1]
steps = list[1:6:2] # (start:stop:step)
print(steps)
print(list, lastElement)

print('-----')

copy = list.copy()
copy.append(True) # add element
copy.insert(1, False) # (index, value): add element with index, prev element shifts
copy.extend([8, 9, 10]) # add multiple elements to end
copy.pop() # (index = -1): remove last element, or index
copy.remove(8) # remove element == 8
print(copy)
copy.clear()

print('-----')

nums = [9, 7, 3, 4, 0, 6, 3, 8, 1, 5, 5]
nums.sort() # returns nothing, works with original array
nums.reverse() # returns nothing, works with original array
print(nums.count(5)) # (element): returns count of element in list
length = len(nums) # return length of list
print(nums, length)

print('----- lists in loops')
for num in nums:
    print(num)

print('----- input length')

lengthOf = int(input('Enter length of list (max: 5): '))
user_result = []


print('for loop: ')

for i in range(0, lengthOf):
  message = 'Enter value #' + str(i + 1) + ': '
  if lengthOf > 5:
    print('Entered value more then 5')
    break
  else:
    value = input(message)
    user_result.append(value)

print('Result: ', user_result)
user_result.clear()

print('while loop: ')
i = 0 

while(i < lengthOf):
  message = 'Enter value #' + str(i + 1) + ': '
  if lengthOf > 5:
    print('Entered value more then 5')
    break
  else:
    value = input(message)
    user_result.append(value)
    i += 1

print('Result: ', user_result)
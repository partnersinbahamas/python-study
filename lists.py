list = [1, 2, 3, 4, 5, [6, 7]]
list[0] = 10
lastElement = list[-1][-1]

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
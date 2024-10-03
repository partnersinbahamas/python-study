def pass_func():
    pass # means nothing or void

def findIndex(list, item):
    index = 0

    for el in list:
        if (el == item):
            return index
        index += 1

    print('Element not exist.')
    return None

nums = [1, 2, 3]
finded = findIndex(nums, 3)
print('finded index: ', finded, nums[finded])

# lambda functions:
# anonimus function
# uses for functions with less funcitonality

lambda_func = lambda list: min(list)
minimal = lambda_func([1, 7, 4])
print(minimal)
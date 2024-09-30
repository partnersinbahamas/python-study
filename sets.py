# Set: returns random sorted with non-repeating chars
data = set('Python')
# data[0] = 0 # will not works

# Methonds
data.add('!')
data.update([True, False])
data.remove(False)
data.pop()

print('set: ', data)

nums = [2, 0, 7, 0, 4]
set_nums = set(nums)

print(nums, set_nums)

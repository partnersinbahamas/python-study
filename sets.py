# Set
# returns random sorted with non-repeating chars

data = set('Python')
# data[0] = 0 # will not works

# Methonds
data.add('!')
data.update([True, False])
data.remove(False)
data.pop()
data.discard('n')

print('set: ', data)

nums = [2, 0, 7, 0, 4]
set_nums = set(nums)

print(nums, set_nums)

# Frozenset: set witch works as a tuple

new_data = frozenset(['Hello', 'world', '!!!'])
print(new_data)

letters = set(['a', 'b', 'c'])
numbers = set([1, 2, 3])
print(letters, numbers)

union_set = letters.union(numbers) # unuin combines both sets
print(union_set)

mod_1 = set([1, 2, 3, 4, 5])
mod_2 = set([1, 2, 3, 6, 7, 8, 9, 10])

mod_12 = mod_1.intersection(mod_2) # returns set of elements witch defined in each of sets

print(mod_12)

bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

bundle_diff = bundle_1.difference(bundle_2) # returns elements with wasnt defined in other set
symm_bundle_diff = bundle_1.symmetric_difference(bundle_2) # returns all elemnts except elements witch was defined

print(bundle_diff)
print(symm_bundle_diff)

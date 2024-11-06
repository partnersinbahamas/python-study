import operator # has much py operations as add, sub...
# more info here https://docs.python.org/3/library/operator.html

# map
toStr = lambda n: str(n)

nums = [1, 2, 3, 4, 5]
naps = map(toStr, nums) # it returns lazy type: <map object at 0x1003e2c10>>
# list(naps) print(*naps)

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

# map with multiple arguments
# here map call lambda func and take iterated argument from odds, evens, nums
calc = map(lambda a, b, c: a + b + c, odds, evens, nums)
print(*calc)

names = ['Denys', 'Danilo', 'Denis']
# methodcaller calls a defined method for each name
uppered = map(operator.methodcaller('upper'), names)
print(*uppered)

# if statement in comprehensions
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_nums = [number for number in numbers if number % 2 == 0]
print(even_nums)

# filter
# is a predicate - the function witch takes any type of argument and returns True or False

# we can do the same action with filter
even_nums_f = list(filter(lambda n: n % 2 == 0, numbers))
print(even_nums_f)

# None in filter means that we want to see only truthy (True) values as result
values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = list(filter(None, values))
print(truthy_values)

from operator import methodcaller

# Iterable Objects
    # Iterable objects are those that can be looped over (for example, in a for loop). Examples of iterable objects include lists, tuples, strings, sets, and dictionaries. These objects can be passed to the iter() function to create an iterator.
    # To be considered an iterable, an object must implement the __iter__() method or have a __getitem__() method that returns values by index

# Iterators
    # An iterator is an object used to access elements of an iterable sequentially. An iterator in Python must implement two methods:

    # __iter__() — returns the iterator itself.
    # __next__() — returns the next element in the sequence, and raises a StopIteration exception when there are no more elements.
    # You can obtain an iterator from an iterable object using the iter() function.

numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

print('iterator: ', next(iterator))


words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller('startswith', 'a'), words)

# in this case, if we want to se our iterators with for loop
# at the end, we gonna se only one print for iterator.

for a in a_words:
    print(a) 

for a in a_words:
    print(a) 

# The reason this happens is because there is nothing left to add to our new list after we have looped through our iterator.
# The values ​​have already been given to us, and the iterator will not give them to us a second time.

print(list(a_words)) # -> []
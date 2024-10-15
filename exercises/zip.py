movie = (
  1, 
  (
    "Eternal Sunshine of the Spotless Mind",
    "Michel Gondry",
    2004
))
# destructurisation
index, (name, film, year) = movie
print(index, name, film, year)

# zip is an extremely powerful and versatile function used to combined two or more iterables into a single iterable.

nums = [1, 2, 3, 4, 5]
strs = ['One', 'Two', 'Free', 'Four', 'Five']

zipped = zip(nums, strs) # (1, 'One'), (2, 'Two'), ...

print(zipped)

for z in zipped:
    print(z)

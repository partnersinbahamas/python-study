# Destructurisation and Zip function
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


# Exercises
# 1. Below is some simple data about characters from BoJack Horseman:
# The data contains the character name, the voice actor or actress who plays them, and the species of the character.
# Write a for loop that uses destructuring so that you can print each tuple in the following format:
# BoJack Horseman is a horse voiced by Will Arnet.
# Note that you're going to have to change the species information to lowercase when you print it. If you need a reminder on how to do this, we covered it in day 3 of the first week.
# 2. Unpack the following tuple into 4 variables:
# The data represents a student's name, their student id number, and their major and minor disciplines in that order.
# 3. Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list containing three items, and a tuples containing four items.
    
var = ("John Smith", 11743, ("Computer Science", "Mathematics"))

name, year, (field, subject) = var

print(name, year, field, subject)
    
main_characters = [
  ("BoJack Horseman", "Will Arnett", "Horse"),
  ("Princess Carolyn", "Amy Sedaris", "Cat"),
  ("Diane Nguyen", "Alison Brie", "Human"),
  ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
  ("Todd Chavez", "Aaron Paul", "Human")
]

def getMovieCharactersInfo(characters):
    for actor, voice_actor, role in characters:
      print(f'{actor} is a {role} voiced by {voice_actor}'.lower())

getMovieCharactersInfo(main_characters)


zip(nums, strs.append('Six')) # NoneType cause nums is length 5 and strs has a 6 lenght



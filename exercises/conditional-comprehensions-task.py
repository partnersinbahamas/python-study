from operator import methodcaller

# Exercises

# 1. Use map to call the strip method on each string in the following list:
# Print the lines of the nursery rhyme on different lines in the console.
# Remember that you can use the operator module and the methodcaller function instead of a lambda expression if you want to.

# 2. Below you'll find a tuple containing several names:
# Use a list comprehension with a filtering condition so that only names with fewer than 8 characters end up in the new list. Make sure that every name in the new list is in title case.

# 3. Use filter to remove all negative numbers from the following range: range(-5, 11). Print the remaining numbers to the console.

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",  
    "    Couldn't put Humpty together again."
]

no_spaces = map(methodcaller('strip'), humpty_dumpty)
print(*no_spaces, sep='\n')

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
fewer_eight = list(filter(lambda name: len(name) < 8, map(methodcaller('title'), names)))

print(fewer_eight)
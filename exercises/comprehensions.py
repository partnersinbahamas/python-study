# Exercises
# 1. Convert the following for loop into a comprehension:

# for number in numbers:
#     squares.append(number ** 2)

# 2) Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.
# Remember that iterating over a dictionary only gives us the keys by default. You can use the items method to get the keys and the values. See day 10 for more details.
# You can find our solutions to the exercises here.


numbers = [1, 2, 3, 4, 5]
squares = [pow(number, 2) for number in numbers]
print(squares)


movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}
updated_movie = {
    key: value.title()
    for key, value in movie.items()
}

print(updated_movie)

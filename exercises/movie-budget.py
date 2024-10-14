# Below you'll find a list which contains the relevant data about a selection of movies. Each item in the list is a tuple containing a movie name and movie budget in that order:
# For this project, your program should do the following:
# 1. Calculate the average budget of all movies in the data set.
# 2. Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
# 3. Print out how many movies spent more than the average you calculated.

movies = [
  ("Eternal Sunshine of the Spotless Mind", 20000000),
  ("Memento", 9000000),
  ("Requiem for a Dream", 4500000),
  ("Pirates of the Caribbean: On Stranger Tides", 379000000),
  ("Avengers: Age of Ultron", 365000000),
  ("Avengers: Endgame", 356000000),
  ("Incredibles 2", 200000000)
]

def movieBudget(movies):
    avarage_sum = 0
    more_then = []
    
    for movie in movies:
        budget = movie[1]
        avarage_sum += budget

    avarage_budget = avarage_sum / len(movies)

    for movie in movies:
        name = movie[0]
        budget = movie[1]

        if budget > avarage_budget:
            print(f'Movie \'{name}\' budget is more then avarage in: {budget - avarage_budget}')
            more_then.append(name)

    # or 
    # more_then = [m[0] for m in movies if m[1] > avarage_budget]
    print(len(more_then))

movieBudget(movies)


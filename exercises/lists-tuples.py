# Exercise
    # 1. Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
    # 2. Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
    # 3. Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
    # 4. Use an f-string to print the movie name and release year by accessing your new movie tuple.
    # 5. Add the new movie tuple to the movies collection using append.
    # 6. Print both movies in the movies collection.
    # 7. Remove the first movie from movies. Use any method you like.

movies = [('Film title', "Autor", 2004)]

def addMovies():
    try:
      film_title = str(input('Enter the film title: '))
      film_autor = str(input('Enter the film autor: '))
      release_year = int(input('Enter the film release year: '))

      new_film = tuple([film_title, film_autor, release_year])
      movies.append(new_film)
      movies.pop(0)
      return f'Your new film: {film_title} by {film_autor} released in {release_year}'
    except ValueError:
       return 'Sorry, values is incorrect.'
    finally:
       print('movies: ', movies)
       print('Close app.')

print(addMovies())

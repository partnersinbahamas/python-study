from typing import Union, Optional, Any

number: int = 1
union: Union[int, float] = 1.23
any: Any = ''

names: list[Union[str, int]] = ['Denys', 20, 'Danil', 20, 'Oleksiy', 20]

Movie_type = tuple[str, str, int]
movies: list[Movie_type] = [
    ("Finding Nemo", "Andrew Stanton", 2005),
    ("Inside Out", "Pete Docter", 2015),
    ("Toy Story 3", "Lee Unkrich", 2010)
]

def showMovies(movies: list[Movie_type], returns: bool = False) -> Union[None, Optional[str]]:
    for title, author, release in movies:
        if returns:
            return f'{title} by {author} in {release} year.'
        else:
            print(f'{title} by {author} in {release} year.')
    return None

showMovies(movies)
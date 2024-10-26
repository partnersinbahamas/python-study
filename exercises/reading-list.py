store = []

menu_promt = """Please select option:
- 'a': to add
- 's': to show store
- 'd': to delete
- 'q': to quit
"""

def add():
    title = input('Title: ').strip().title()
    author = input('Author: ').strip().title()
    year = int(input('Release year: ').strip())

    book = dict(title=title, author=author, year=year)
    store.append(book)

    print('Adding...')

def remove():
    for i, book in enumerate(store):
      print(i, book.get('title'))

    user_index = int(input('Please select book index: ').strip())

    for i, book in enumerate(store):
        if user_index == i:
            store.pop(i)

def show():
    if len(store) <= 0:
        print('Store is empty.')

    for book in store:
        title = book.get('title')
        author = book.get('author')
        year = book.get('year')
        
        print(f'{title} by {author} in {year}')

def menu():
    user_option = input(menu_promt).strip().lower()

    if user_option == 'q': listener()

    if user_option == 'a':
        add()
    elif user_option == 'd':
        remove()
    elif user_option == 's':
        show()


def listener():
    start_or_stop = input('Press "Y" to start or "N" to stop: ').lower()

    while start_or_stop != 'n':
        menu()
    else: 
        print('Close thea app.')

listener()


    
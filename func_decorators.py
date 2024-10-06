import webbrowser as wb
# Descorators uses to modify or extend the behavior of functions or methods without changing their code.

def validator(func):
    def wrapper(url):
        if ('https://' in url):
            func(url)
        else:
            print('Invalid URL address.')
    return wrapper

@validator
def open_url(url):
    wb.open(url)

open_url('https://www.npmjs.com/package/2ra-ui')
import webbrowser as wb
from typing import Callable
from functools import wraps
# Descorators uses to modify or extend the behavior of functions or methods without changing their code.

# decorator
def validator(func: Callable) -> Callable:
    # Using wraps, we can preserve the original function name, and importantly, any documentation included in that function.
    @wraps(func)
    def wrapper(url):
        if ('https://' in url):
            func(url)
        else:
            print('Invalid URL address.')
    return wrapper

@validator
def open_url(url):
    wb.open(url)

# open_url('https://www.npmjs.com/package/2ra-ui')
    
# with @wraps: <function open_url at 0x100cad5e0>
# without: <function validator.<locals>.wrapper at 0x1046215e0>
print(open_url)
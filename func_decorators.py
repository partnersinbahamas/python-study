import webbrowser as wb
from typing import Callable
from functools import wraps
from time import perf_counter
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

# decorator
def timewatch(func: Callable) -> Callable:
    def inner(*args):
        # By calling perf_counter, running our code, and calling perf_counter again, we can get a good idea of the time that elapsed between the two called to perf_counter.
        start_time = perf_counter()
        func(*args)
        end_time = perf_counter()

        print(f'{func.__name__} ended in {end_time - start_time:.5f}')
    return inner

@timewatch
@validator
def open_url(url):
    wb.open(url)

open_url('https://www.npmjs.com/package/2ra-ui')
    
# with @wraps: <function open_url at 0x100cad5e0>
# without: <function validator.<locals>.wrapper at 0x1046215e0>
print(open_url)
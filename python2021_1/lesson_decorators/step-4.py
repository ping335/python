"""
Декораторы с параметрами.

def parametrize(<параметры_декоратора>):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
"""

from functools import wraps
from textwrap import dedent
from datetime import datetime


def log(filename):
    template = dedent('''
    [{now:%Y-%m-%d %H:%M:%S}] Function "{func}" called with:
        -> positional arguments: {args}
        -> keyword arguments:    {kwargs}
    Returns: {result}
    ''')
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'a') as f:
                f.write(template.format(
                    now=datetime.now(),
                    func=f'{func.__module__}.{func.__qualname__}',
                    args=args,
                    kwargs=kwargs,
                    result=result
                ))
            return result
        return wrapper
    
    return decorator


@log('log.txt')
def f(a, b):
    return a + b

print(f(1, 5))
print(f('a', 'b'))

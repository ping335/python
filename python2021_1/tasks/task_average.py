"""
if connect():
    if select_db():
        if query():
            do
        else:
            raise QueryError
    else:
        raise DBError
else:
    raise ConnectError


if not connect():
    raise ConnectError

if not select_db():
    raise DBError

if not query():
    raise QueryError

do
"""

def average(lst):
    if not lst:
        raise ArithmeticError('The list must contain at least one item')
    return round(sum(lst) / len(lst), 3)

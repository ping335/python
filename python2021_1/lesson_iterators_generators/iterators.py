"""
Итераторы

iter(obj[, sentinel]) -> Iterator
__iter__
__getitem__
"""

import hashlib


s = 'Говорящий хомячок'
lst = ['Хома', 'Сеня', 'Роза', 'Соня']
product = {
    'name': 'Колесико',
    'price': 1499.99,
    'count': 10,
}

it = iter(s)
it = iter(lst)
it = iter(product)
it = iter(product.values())
it = iter(product.items())
print(it, type(it))
print(next(it), next(it), next(it))
# print(next(it))


# for i in product:
#     print(i)
it = iter(product)
while 1:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break

with open(__file__) as f:
    it = iter(f)
    print(f, it)
    print(next(it), next(it))
    for line in f:
        print(line)
        break


def md5file(filename):
    """Возвращает хеш сумму по содержимому указанного файла."""
    with open(filename, 'rb') as f:
        return md5stream(f)


def md5stream(stream):
    """Возвращает хеш сумму по потоку данных."""
    hash_md5 = hashlib.md5()
    pos = stream.tell()
    
    for chunk in iter(lambda: stream.read(4096), b''):
        hash_md5.update(chunk)
    
    stream.seek(pos)
    
    return hash_md5.hexdigest()


print(f'MD5 сумма файла лекции: {md5file(__file__)}')






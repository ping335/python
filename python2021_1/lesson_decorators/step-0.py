"""Замыкания"""

from urllib.request import urlopen


def page(url):
    def get():
        return urlopen(url).read()
    return get


python = page('http://python.org')
print(python, type(python))
print(python())

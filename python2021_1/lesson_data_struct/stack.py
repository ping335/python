"""Стек"""

from linked_list import LinkedList


class StackError(Exception):
    def __init__(self, stack, message=''):
        super().__init__(message)
        self.stack = stack


class StackOverflow(StackError):
    """Переполнение стека"""


class StackUnderflow(StackError):
    """Стек пуст"""


class Stack:
    """Стек на базе односвязного списка"""
    
    def __init__(self, max_length=0):
        self.list = LinkedList()
        self.max_length = max_length
    
    def is_empty(self):
        """Возвращает истину, если стек пустой."""
        return self.list.is_empty()
    
    def push(self, value):
        """Добавляет элемент в стек."""
        if 0 < self.max_length <= self.list.length():
            raise StackOverflow(self)
        self.list.insert(value) # всегда O(1)
    
    def pop(self):
        """Удалить элемент из стека и вернуть значение."""
        if self.is_empty():
            raise StackUnderflow(self)
        return self.list.remove_head()


if __name__ == '__main__':
    s = Stack(max_length=3)
    s.push(10)
    s.push(20)
    s.push(30)
    
    try:
        # print(s.push(666))
        print(s.pop(), s.pop(), s.pop(), s.pop())
    except StackOverflow as err:
        print(err.stack.max_length)
    except StackUnderflow as err:
        print(err.stack.is_empty())

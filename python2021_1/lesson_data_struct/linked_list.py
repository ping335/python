"""Односвязный список"""

class Node:
    """Узел списка"""
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_
    
    def __repr__(self):
        return f'<{self.__class__.__name__} value={self.value!r}>'


class LinkedList:
    """Односвязный список"""
    
    def __init__(self):
        self.head = None # голова списка
        self.tail = None # хвост списка
        self.size = 0    # размер списка
        
    def __repr__(self):
        nodes = ', '.join(repr(i.value) for i in self.nodes())
        return f'<{self.__class__.__name__} values=({nodes})>'
    
    def _create(self, value):
        """Создает и возвращает новый узел списка с указанными данными."""
        return Node(value)
    
    def _get_prev(self, node):
        """Возвращает предыдущий узел для указанного узла списка."""
        if node is self.head:         # если указанный узел это голова,
            return None               # то предыдущего узел не существует
        
        for current in self.nodes():  # итерируемся узла списка
            if current.next is node:  # проверяем является ли следующий узел за текущим - искомым
                return current        # возвращаем текущий узел, как предыдущий
        
        raise ValueError(f'{node!r} not found in the current linked list.')
    
    def is_empty(self):
        """Возвращает истину, если список пустой, иначе ложь."""
        return self.head is None
    
    def length(self):
        """Возвращает длину списка."""
        return self.size
    
    def nodes(self):
        """Возвращает генератор из узлов списка."""
        current = self.head         # начинаем итерирование узлов с головы
        while current is not None:  # пока счетчик ссылается на узел
            yield current           # выбрасываем из генератора узел
            current = current.next  # теперь счетчик ссылается на следующий узел текущего
    
    def append(self, value):
        """Создает и добавляет узел в конец списка, а затем возвращает добавленный узел."""
        return self.insert(value, self.tail)
    
    def insert(self, value, node=None):
        """
        Создает и добавляет узел после указанного узла и возвращает добавленый узел.
        Если узел не передается, добавление нового узла происходит в начало списка.
        """
        current = self._create(value)
        
        if node is None:                         # заменяем голову списка
            if self.is_empty():                  # если список пустой
                self.head = self.tail = current  # то задаем ссылки на новую голову и хвост
            else:
                current.next = self.head         # иначе текущий узел ссылается на старую голову
                self.head = current              # и сам становится головой
        else:
            if node.next is None:                # если вставка в конец списка,
                self.tail = current              # то текущий элемент становится хвостом
            else:
                current.next = node.next         # текущий узел ссылается на следующий узел переданного
            
            node.next = current                  # переданный узел ссылается на текущий
        
        self.size += 1
        
        return current
    
    def remove(self, node):
        """Удаляет указанный узел из списка и возвращает данные узла."""
        if self.is_empty():  # если список пустой, то удалять нечего
            raise ValueError('Linked list is empty.')
        
        prev = self._get_prev(node) # получаем ссылку на предыдущий узел
        
        if prev is None:            # если предыдущего узла нет, то удаляем голову,
            self.head = node.next   # заменяем голову на следующий узел переданного
        else:
            prev.next = node.next   # иначе предыдущему узлу меняем ссылку на следующий узел
                                    # как следующий узел удаляемого узла
        
        if node is self.tail:       # если удаляемый узел это хвост
            self.tail = prev        # то новый хвост - предыдущий узел
        
        self.size -= 1
        
        return node.value           # возвращаем данные узла
    
    def remove_head(self):
        """Удаляет первый узел из списка и возвращает данные узла."""
        return self.remove(self.head)
    
    def remove_tail(self):
        """Удаляет последний узел из списка и возвращает данные узла."""
        return self.remove(self.tail)
    
    def search(self, value):
        """Находит и возвращает первый узел с указанным значением, либо None."""
        for node in self.nodes():    # итерируемся по узлам списка
            if node.value == value:  # если значение узла совпадает и искомым,
                return node          # то возвращаем узел


if __name__ == '__main__':
    ll = LinkedList()
    
    node1 = ll.append(0)
    print(node1)
    
    node2 = ll.insert(1)
    print(node2)
    
    node3 = ll.insert(2, node1)
    print(node3)
    
    print(ll)
    
    print(ll.remove(node1), ll)
    print(ll.remove_tail(), ll)
    print(ll.remove_head(), ll)
    
    # ll.remove_head()

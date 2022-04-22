def final(obj):
    obj._isfinal_ = True
    return obj


class FinalMeta(type):
    def __new__(mcs, name, bases, d):
        for base in bases:
            if isinstance(base, mcs):
                if hasattr(base, '_isfinal_'):
                    raise TypeError(f'Class {base.__qualname__} is final.')
                
                methods = (getattr(base, name, None) for name, attr in d.items() if callable(attr))
                
                for method in methods:
                    if method and hasattr(method, '_isfinal_'):
                        raise TypeError(f'Method {method.__qualname__} is final.')
        
        return super().__new__(mcs, name, bases, d)


@final
class Product(metaclass=FinalMeta):
    def __init__(self, name):
        self._name = name
    
    # @final
    def get_name(self):
        return self._name


class Tomato(Product):
    pass
    # def get_name(self):
    #     return self._name * 2
